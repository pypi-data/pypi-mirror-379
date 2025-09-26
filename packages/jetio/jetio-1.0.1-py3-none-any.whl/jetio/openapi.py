"""
OpenAPI (Swagger) schema generation for the Jetio framework.

This module provides functions to automatically generate an OpenAPI 3.0 schema
from the routes and models defined in a Jetio application. This enables
automatic interactive API documentation via tools like Swagger UI.
"""

import inspect
import re # <-- NEW IMPORT
from enum import Enum
from typing import get_origin, get_args, List
from pydantic import BaseModel
from pydantic.json_schema import model_json_schema
from sqlalchemy.orm import Session
from .framework import Jetio, JsonResponse, Response, Request
from .orm import _model_registry

def _generate_and_add_schema(model, schema_store):
    """
    Generates a Pydantic model's JSON schema and adds it to the store.

    This is a helper function to avoid duplicating schema definitions.

    Args:
        model: The Pydantic model class.
        schema_store: The dictionary where schemas are stored (part of the main OpenAPI spec).

    Returns:
        The name of the schema if generated, otherwise None.
    """
    if not model or not inspect.isclass(model) or not issubclass(model, BaseModel):
        return None
        
    schema_name = model.__name__
    if schema_name not in schema_store:
        # Generate the JSON schema for the model.
        model_schema = model_json_schema(model, ref_template="#/components/schemas/{model}")
        
        # Pydantic v2 can create a '$defs' section for nested models.
        if '$defs' in model_schema:
            for def_name, def_schema in model_schema['$defs'].items():
                if def_name not in schema_store:
                    schema_store[def_name] = def_schema
            del model_schema['$defs']

        schema_store[schema_name] = model_schema
    
    return schema_name

def generate_openapi_schema(app: Jetio):
    """
    Inspects the application's models and route signatures to create an OpenAPI schema.

    Args:
        app: The main `Jetio` application instance.

    Returns:
        A dictionary representing the complete OpenAPI 3.0 specification.
    """
    schema = {
        "openapi": "3.0.0",
        "info": {
            "title": app.title,
            "version": app.version,
            "description": "Auto-generated API documentation by the Jetio Framework."
        },
        "paths": {},
        "components": {"schemas": {}}
    }
    schema_store = schema['components']['schemas']

    # First, generate schemas for all registered JetioModels.
    for model in _model_registry:
        if hasattr(model, '__pydantic_read_model__'):
            _generate_and_add_schema(model.__pydantic_read_model__, schema_store)
        if hasattr(model, '__pydantic_create_model__'):
            _generate_and_add_schema(model.__pydantic_create_model__, schema_store)
        
    # Then, iterate through all registered routes to build the 'paths' section.
    for route in app.routes:
        handler = route.handler
        sig = inspect.signature(handler)
        
        # This regex correctly converts paths like "/users/{user_id:int}"
        # into the standard OpenAPI format "/users/{user_id}", which allows the
        # Swagger UI to generate the correct input fields.
        openapi_path = re.sub(r':\w+}', '}', route.path)

        if openapi_path not in schema['paths']:
            schema['paths'][openapi_path] = {}

        for method in route.methods:
            method_lower = method.lower()
            operation = {
                "summary": (inspect.getdoc(handler) or "No summary").split('\n')[0],
                "tags": [openapi_path.strip('/').split('/')[0].title()],
                "responses": {"200": {"description": "Successful Response"}}
            }

            # --- Parameters (Path and Body) ---
            # This regex finds all parameter names within curly braces.
            path_param_names = re.findall(r'{(\w+)', openapi_path)
            operation['parameters'] = []

            for name, param in sig.parameters.items():
                if name in path_param_names:
                    # Handle path parameters (e.g., {item_id:int}).
                    operation['parameters'].append({
                        "name": name, "in": "path", "required": True,
                        "schema": {"type": "integer" if param.annotation is int else "string"}
                    })
                elif isinstance(param.annotation, type) and issubclass(param.annotation, BaseModel):
                    # Handle request body (Pydantic models).
                    schema_name = _generate_and_add_schema(param.annotation, schema_store)
                    if schema_name:
                        operation['requestBody'] = {
                            "required": True,
                            "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{schema_name}"}}}
                        }
            
            # --- Responses ---
            if sig.return_annotation != inspect.Signature.empty:
                response_model = sig.return_annotation
                status_code = "201" if method == "POST" else "200"
                response_schema = {}

                origin = get_origin(response_model)
                if origin is list or origin is List:
                    # Handle list responses (e.g., List[UserRead]).
                    item_model = get_args(response_model)[0]
                    if hasattr(item_model, '__pydantic_read_model__'):
                        item_model = item_model.__pydantic_read_model__
                    
                    item_schema_name = _generate_and_add_schema(item_model, schema_store)
                    if item_schema_name:
                        response_schema = { "type": "array", "items": {"$ref": f"#/components/schemas/{item_schema_name}"} }
                else:
                    # Handle single item responses.
                    if hasattr(response_model, '__pydantic_read_model__'):
                        response_model = response_model.__pydantic_read_model__
                    
                    schema_name = _generate_and_add_schema(response_model, schema_store)
                    if schema_name:
                        response_schema = {"$ref": f"#/components/schemas/{schema_name}"}

                if response_schema:
                    operation['responses'][status_code] = { "description": "Successful Response", "content": {"application/json": {"schema": response_schema}} }
            
            schema['paths'][openapi_path][method_lower] = operation
    return schema

def add_swagger_ui(app):
    """
    A helper function that adds the /docs and /openapi.json routes to a Jetio app.

    This makes it easy to add interactive API documentation to any application.

    Args:
        app: The `Jetio` application instance.
    """
    @app.route('/docs')
    def swagger_ui(request: Request):
        """Serves the Swagger UI HTML page."""
        # Get the root path from the request's scope. This will be something like
        # "/jetio_app" when deployed in a sub-directory on cPanel.
        root_path = request._scope.get("root_path", "")
        # Construct the correct, full URL for the openapi.json file.
        # This ensures Swagger UI can find the spec file regardless of deployment environment.
        openapi_url = f"{root_path}/openapi.json"

        html_content = f"""
        <!DOCTYPE html>
        <html><head><title>{app.title} - Docs</title><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css"></head>
        <body><div id="swagger-ui"></div><script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
        <script>SwaggerUIBundle({{url: "{openapi_url}", dom_id: '#swagger-ui'}})</script></body></html>
        """
        return Response(html_content)

    @app.route('/openapi.json')
    def openapi_spec(request: Request):
        """Serves the auto-generated OpenAPI JSON schema."""
        schema = generate_openapi_schema(app)

        # Dynamically add the server URL based on the deployment's root_path.
        # This tells Swagger UI to prefix all API calls with the sub-directory path
        # (e.g., /jetio_app), fixing the 404 errors when trying out endpoints.
        root_path = request._scope.get("root_path", "")
        if root_path:
            schema["servers"] = [{"url": root_path}]

        return JsonResponse(schema)