from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Type

from commonmark import commonmark
from pydantic import BaseModel, RootModel

from lamina import conf
from lamina.openapi.types import (
    ComponentsObject,
    OpenAPIContactObject,
    OpenAPIExternalDocumentationObject,
    OpenAPIInfoObject,
    OpenAPILicenseObject,
    OpenAPIObject,
    OpenAPIServerObject,
    OperationObject,
    RequestBodyObject,
    ResponseObject,
)
from lamina.openapi.view_data import ViewData, extract_schema_info


@dataclass
class SwaggerGenerator:
    """OpenAPI 3.1 generator for lamina-decorated handlers.

    This class inspects the global LAMINA_REGISTRY to build an OpenAPI
    specification from the Pydantic schemas and metadata attached via
    json_schema_extra, mirroring the behavior of the legacy
    get_openapi_spec function while providing a more structured design.

    Attributes:
        openapi_version: OpenAPI version string (default: 3.1.0).
        json_schema_dialect: Optional custom JSON Schema dialect URI.
        view_docstring: Optional docstring to extract title/description when
            generating an info object for a single-view use case.
    """

    view_data: List[ViewData]
    extra_data: Dict[str, Any] = None
    openapi_version: str = "3.1.0"
    json_schema_dialect: str | None = None

    @staticmethod
    def _get_model_schema_ref(
        model: Type[BaseModel | RootModel],
    ) -> Tuple[str, Dict[str, Any]]:
        """Return the JSON Schema reference name and full schema for the  model."""
        schema = model.model_json_schema(ref_template="#/components/schemas/{model}")
        name = schema.get("title") or model.__name__
        return name, schema

    def _content_for_model(
        self,
        model: Optional[Type[BaseModel | RootModel]],
    ) -> Optional[dict]:
        if model is None:
            return None
        name, _ = self._get_model_schema_ref(model)
        return {
            "application/json": {"schema": {"$ref": f"#/components/schemas/{name}"}}
        }

    @staticmethod
    def get_info(
        *,
        title: str,
        version: str,
        summary: str | None = None,
        description: str | None = None,
        contact: OpenAPIContactObject | None = None,
        license_info: OpenAPILicenseObject | None = None,
        terms_of_service: str | None = None,
    ) -> OpenAPIInfoObject:
        """Build the OpenAPI Info object using provided values."""
        info: OpenAPIInfoObject = {"title": title, "version": version}
        if summary:
            info["summary"] = summary
        if description:
            info["description"] = commonmark(description)
        if contact:
            info["contact"] = contact
        if license_info:
            info["license"] = license_info
        if terms_of_service:
            info["termsOfService"] = terms_of_service
        return info

    @staticmethod
    def get_servers(
        host: str | None = None,
        base_path: str = "/",
        servers: List[OpenAPIServerObject] | None = None,
    ) -> List[OpenAPIServerObject] | None:
        """Build a server list from explicit servers or host/base_path."""
        server_objs = None
        if conf.LAMINA_API_URL:
            server_objs = [{"url": conf.LAMINA_API_URL}]
        elif servers:
            server_objs = servers
        elif host:
            bp = base_path or "/"
            url = f"{host}{bp}"
            if not url.startswith("http"):
                url = f"https://{url}"
            server_objs = [{"url": url}]
        return server_objs

    def get_responses(self, view):
        responses: Dict[str, ResponseObject] = {}
        response_content = self._content_for_model(view.response)
        responses[str(conf.LAMINA_DEFAULT_SUCCESS_STATUS_CODE)] = ResponseObject(
            **{
                "description": view.extract_extras().get(
                    "response_description", "Successful Response"
                ),
                "content": response_content
                or {"application/json": {"schema": {"type": "string"}}},
            }
        )
        responses["400"] = {"description": "Bad Request"}
        responses["500"] = {"description": "Internal Server Error"}

        # Custom responses from decorator
        custom_responses = view.extra_responses or {}
        for status_code, cfg in custom_responses.items():
            code_str = str(status_code)
            schema_model = cfg.get("schema") if isinstance(cfg, dict) else None
            desc = cfg.get("description") if isinstance(cfg, dict) else None
            content = None
            if schema_model is not None:
                name, _schema_def = extract_schema_info(schema_model)
                content = {
                    "application/json": {
                        "schema": {"$ref": f"#/components/schemas/{name}"}
                    }
                }
            response_obj: ResponseObject = {"description": desc or "Response"}
            if content:
                response_obj["content"] = content
            responses[code_str] = response_obj
        return responses

    def get_paths(self) -> Dict[str, Dict[str, OperationObject]] | None:
        """Assemble the OpenAPI paths and operations from LAMINA_REGISTRY."""
        paths: Dict[str, Dict[str, OperationObject]] = {}

        for view in self.view_data:
            request_body_content = self._content_for_model(view.request)
            path = view.get_path()
            methods = view.get_methods()

            operation: OperationObject = {
                "summary": view.get_summary(),
                "description": view.get_description(),
                "operationId": view.get_operation_id(),
                "parameters": view.get_parameters(),
                "responses": self.get_responses(view),
                "tags": view.get_tags(),
            }
            if request_body_content:
                operation["requestBody"] = RequestBodyObject(
                    **{
                        "content": request_body_content,
                        "required": True,
                    }
                )

            if path not in paths:
                paths[path] = {}
            for method in methods:
                paths[path][method] = operation

        return paths

    @staticmethod
    def get_webhooks() -> Dict[str, Any] | None:
        """No webhooks currently generated."""
        return None

    def get_components(
        self, security_schemes: Optional[Dict[str, Any]] | None = None
    ) -> ComponentsObject | None:
        """Build the Components object (schemas and securitySchemes).

        Collects schemas from request/response/params models and from any custom
        response schemas declared via the decorator.
        """
        schemas: Dict[str, Any] = {}

        for view in self.view_data:
            view_schemas = view.resolve_schemas()

            # Process each schema to extract $defs
            for name, schema in view_schemas.items():
                schemas[name] = schema

                # Extract and promote $defs to global schemas
                if "$defs" in schema:
                    defs = schema.pop("$defs")  # Remove $defs from original schema
                    for def_name, def_schema in defs.items():
                        if def_name not in schemas:
                            schemas[def_name] = def_schema

        if security_schemes is None:
            security_schemes = {
                "ApiKeyAuth": {
                    "type": "apiKey",
                    "in": "header",
                    "name": conf.LAMINA_DEFAULT_AUTH_HEADER_NAME,
                }
            }

        if not schemas and not security_schemes:
            return None
        return ComponentsObject(
            **{"schemas": schemas, "securitySchemes": security_schemes}
        )

    def get_security(
        self,
        security: Optional[List[Dict[str, List[str]]]] | None = None,
    ) -> List[Dict[str, List[str]]] | None:
        """Return global security requirements."""
        if security:
            return security

        components = self.get_components()
        security_schemes = components.get("securitySchemes")

        if security_schemes:
            return [{name: []} for name in security_schemes.keys()]
        return None

    @staticmethod
    def get_tags() -> List[Dict[str, str]] | None:
        """No top-level tags aggregation yet."""
        return None

    def generate(
        self,
        title: str,
        version: str,
        host: str | None = None,
        base_path: str | None = None,
        servers: OpenAPIServerObject | None = None,
        summary: str | None = None,
        description: str | None = None,
        contact: OpenAPIContactObject | None = None,
        license_info: OpenAPILicenseObject | None = None,
        terms_of_service: str | None = None,
        security_schemes: Optional[Dict[str, Any]] | None = None,
        security: Optional[List[Dict[str, List[str]]]] = None,
        external_docs: Optional[OpenAPIExternalDocumentationObject] | None = None,
    ) -> OpenAPIObject:
        """Generate an OpenAPI specification using the class helpers."""
        spec: OpenAPIObject = {
            "openapi": self.openapi_version,
            "info": self.get_info(
                title=title,
                version=version,
                summary=summary,
                description=description,
                contact=contact,
                license_info=license_info,
                terms_of_service=terms_of_service,
            ),
        }
        if self.json_schema_dialect:
            spec["jsonSchemaDialect"] = self.json_schema_dialect
        if servers := self.get_servers(host, base_path or "/", servers):
            spec["servers"] = servers
        paths = self.get_paths()
        spec["paths"] = paths or {}
        if components := self.get_components(security_schemes):
            spec["components"] = components
        if security := self.get_security(security=security):
            spec["security"] = security
        if external_docs:
            spec["externalDocs"] = external_docs
        return spec
