"""
The core of the Jetio web framework.

This module contains the main `Jetio` application class, along with the `Request`
and `Response` objects that form the foundation of the framework's HTTP handling.
It provides routing, dependency injection, and basic request/response processing.
"""

import json
import inspect
import asyncio
import uvicorn
import logging
import re 
from jinja2 import Environment, FileSystemLoader
from http.cookies import SimpleCookie
from pydantic import BaseModel, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from starlette.formparsers import MultiPartParser
from starlette.datastructures import UploadFile, Headers

from .orm import SessionLocal, JetioModel

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# A class to handle dependency injection more robustly.
class Depends:
    """
    A marker class for dependency injection.

    When used as a default value for a route handler parameter, the framework
    will call the provided dependency function and inject its return value.

    Example:
        async def get_current_user(request: Request) -> User:
            ...

        @app.route('/profile')
        async def profile(user: User = Depends(get_current_user)):
            return {"username": user.username}
    """
    def __init__(self, dependency: callable):
        """
        Args:
            dependency: The callable (function or class) to be resolved.
        """
        self.dependency = dependency

class Request:
    """
    Represents an incoming HTTP request.

    It provides access to the request method, path, headers, cookies,
    and body content (JSON, form data, etc.). An instance of this class
    is passed to every route handler.
    """
    def __init__(self, scope, receive):
        """
        Initializes a Request object.

        Args:
            scope: The ASGI scope dictionary.
            receive: The ASGI receive awaitable.
        """
        self._scope = scope
        self._receive = receive
        self._stream_consumed = False
        self._form = None
        self._json = None
        self.method = scope['method']

        # Handle root_path for deployments in a sub-directory (e.g., on cPanel).
        # The ASGI server provides a 'root_path' which we need to strip from the
        # beginning of the full path to get the path relative to the app.
        root_path = scope.get("root_path", "")
        path = scope.get("path", "/")
        if root_path and path.startswith(root_path):
            self.path = path[len(root_path):] or "/"
        else:
            self.path = path

        self.headers = Headers(scope=scope)
        self.cookies = SimpleCookie(self.headers.get('cookie', ''))
        self.user = None

    async def stream(self):
        """Reads the incoming request body as a stream of bytes."""
        if self._stream_consumed:
            yield b''
            return
        self._stream_consumed = True
        while True:
            message = await self._receive()
            if message['type'] == 'http.request':
                yield message.get('body', b'')
                if not message.get('more_body', False):
                    break
        yield b''

    async def body(self) -> bytes:
        """Reads the entire request body into a single bytes object."""
        if hasattr(self, '_body'):
            return self._body
        chunks = [chunk async for chunk in self.stream()]
        self._body = b"".join(chunks)
        return self._body

    async def json(self):
        """Parses the request body as JSON."""
        if self._json is None:
            body_bytes = await self.body()
            try:
                self._json = json.loads(body_bytes) if body_bytes else {}
            except (json.JSONDecodeError, TypeError):
                self._json = {}
        return self._json

    async def form(self):
        """Parses the request body as form data (multipart/form-data)."""
        if self._form is not None:
            return self._form
        parser = MultiPartParser(headers=self.headers, stream=self.stream())
        self._form = await parser.parse()
        return self._form

class Response:
    """
    Represents an outgoing HTTP response.

    It encapsulates the response body, status code, and headers.
    """
    def __init__(self, body='', status_code=200, content_type='text/html', headers=None):
        """
        Initializes a Response object.

        Args:
            body: The response body, as a string.
            status_code: The HTTP status code.
            content_type: The value of the Content-Type header.
            headers: A dictionary of additional response headers.
        """
        if isinstance(body, str):
            self.body = body.encode('utf-8')
        else:
            self.body = body # Assume it's already bytes

        self.status_code = status_code
        self.headers = headers or {}
        self.headers.setdefault('Content-Type', content_type)
        self.headers.setdefault('Content-Length', str(len(self.body)))

    async def __call__(self, scope, receive, send):
        """The ASGI callable interface."""
        await send({'type': 'http.response.start', 'status': self.status_code, 'headers': [[k.encode(), v.encode()] for k, v in self.headers.items()]})
        await send({'type': 'http.response.body', 'body': self.body})


class JsonResponse(Response):
    """
    A specialized Response class for sending JSON data.

    It automatically serializes Python objects (including Pydantic models)
    to a JSON string and sets the Content-Type header to 'application/json'.
    """
    def __init__(self, data, status_code=200, **kwargs):
        """
        Initializes a JsonResponse object.

        Args:
            data: The Python object to serialize to JSON.
            status_code: The HTTP status code.
            **kwargs: Additional arguments for the parent Response class.
        """
        def pydantic_encoder(obj):
            if isinstance(obj, BaseModel):
                return obj.model_dump(mode='json')
            # This is the key change. The framework now knows how to handle
            # raw SQLAlchemy model instances by using their auto-generated
            # Pydantic 'Read' schema for serialization.
            if isinstance(obj, JetioModel):
                return obj.__pydantic_read_model__.model_validate(obj, from_attributes=True).model_dump(mode='json')
            return str(obj)
        json_body = json.dumps(data, indent=2, default=pydantic_encoder)
        super().__init__(body=json_body, status_code=status_code, content_type='application/json', **kwargs)


class BaseMiddleware:
    """Base class for creating custom middleware."""
    def __init__(self, app): self.app = app
    async def __call__(self, scope, receive, send): await self.app(scope, receive, send)

# --- Custom Exception Classes ---
class MethodNotAllowedError(Exception):
    """Raised when a request is made to a valid path with an invalid HTTP method."""
    pass
class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass
class HttpValidationError(Exception):
    """Raised when Pydantic validation of request body fails."""
    def __init__(self, errors): self.errors = errors

class Jetio:
    """
    The main application class for the Jetio framework.

    This class acts as the central hub for routing, middleware, and request handling.
    It is an ASGI-compliant application.
    """
    def __init__(self, title: str = "Jetio API", version: str = "1.0.0", template_folder='templates'):
        """
        Initializes the Jetio application.

        Args:
            title: The title of the API, used in OpenAPI documentation.
            version: The version of the API, used in OpenAPI documentation.
            template_folder: The directory where HTML templates are stored.
        """
        self.routes = []
        self.title = title
        self.version = version
        self.template_env = Environment(loader=FileSystemLoader(template_folder), autoescape=True)
        self.error_handlers = {}
        self.startup_handlers = []
        self.shutdown_handlers = []
        self.app = self.handle_request

    def add_middleware(self, middleware_cls, **kwargs):
        """
        Adds a middleware to the application stack.

        Middleware is processed in reverse order of addition.

        Args:
            middleware_cls: The middleware class to add.
            **kwargs: Keyword arguments to pass to the middleware constructor.
        """
        self.app = middleware_cls(self.app, **kwargs)

    def add_error_page(self, status_code: int, template_name: str):
        """
        Registers a custom HTML template for a specific HTTP error status code.

        Args:
            status_code: The HTTP status code (e.g., 404, 500).
            template_name: The filename of the template in the template folder.
        """
        self.error_handlers[status_code] = template_name

    def route(self, path, methods=None):
        """
        A decorator to register a view function for a given URL path.

        Args:
            path: The URL path string. Can include placeholders like `{user_id:int}`.
            methods: A list of allowed HTTP methods (e.g., ['GET', 'POST']).
                     Defaults to ['GET'].

        Returns:
            A decorator that registers the function.
        """
        def wrapper(handler):
            self.routes.append(Route(path, handler, methods or ['GET']))
            return handler
        return wrapper

    def on_event(self, event_type: str):
        """A decorator to register a startup or shutdown event handler."""
        def wrapper(handler):
            if event_type == "startup":
                self.startup_handlers.append(handler)
            elif event_type == "shutdown":
                self.shutdown_handlers.append(handler)
            return handler
        return wrapper

    async def __call__(self, scope, receive, send):
        """The main ASGI entry point for the application."""
        # NEW: Added a check to provide a helpful error if run by a WSGI server.
        # A valid ASGI scope is a dictionary with a 'type' key.
        # A WSGI environ dictionary does not have 'type' but has 'wsgi.version'.
        if not isinstance(scope, dict) or 'type' not in scope:
            if isinstance(scope, dict) and 'wsgi.version' in scope:
                # This is a WSGI environment. Raise a specific, helpful error.
                raise TypeError(
                    "This is an ASGI application, but it was called by a WSGI server.\n"
                    "Please check your server's entry point (e.g., passenger_wsgi.py) "
                    "and ensure you are using an ASGI-to-WSGI adapter like 'a2wsgi'."
                )
            # If it's not ASGI or WSGI, raise a generic error.
            raise TypeError("Invalid ASGI scope provided to application. Expected a dictionary with a 'type' key.")

        if scope['type'] == 'lifespan':
            while True:
                message = await receive()
                if message['type'] == 'lifespan.startup':
                    try:
                        for handler in self.startup_handlers:
                            await handler()
                        await send({'type': 'lifespan.startup.complete'})
                    except Exception as e:
                        log.exception("Error during startup.")
                        await send({'type': 'lifespan.startup.failed', 'message': str(e)})
                elif message['type'] == 'lifespan.shutdown':
                    try:
                        for handler in self.shutdown_handlers:
                            await handler()
                        await send({'type': 'lifespan.shutdown.complete'})
                    except Exception as e:
                        log.exception("Error during shutdown.")
                        await send({'type': 'lifespan.shutdown.failed', 'message': str(e)})
                    return
        elif scope['type'] == 'http':
            await self.app(scope, receive, send)

    async def handle_request(self, scope, receive, send):
        """
        The core request handling logic.

        This method finds a matching route, resolves dependencies, calls the
        handler, and sends the response. It also handles exceptions and
        manages the database session lifecycle.
        """
        db_session = SessionLocal()
        try:
            request = Request(scope, receive)
            handler, path_kwargs = self.find_handler(request.path, request.method)

            # --- Dependency Injection and Argument Resolution ---
            sig = inspect.signature(handler)
            handler_kwargs = {}
            for name, param in sig.parameters.items():
                if name in path_kwargs:
                    param_type = param.annotation
                    if param_type is not inspect.Parameter.empty:
                        handler_kwargs[name] = param_type(path_kwargs[name])
                    else:
                        handler_kwargs[name] = path_kwargs[name]
                elif param.annotation is Request:
                    # Inject the Request object
                    handler_kwargs[name] = request
                elif param.annotation is AsyncSession:
                    # Inject the database session
                    handler_kwargs[name] = db_session
                elif isinstance(param.annotation, type) and issubclass(param.annotation, BaseModel):
                    # Inject and validate Pydantic model from request body
                    try:
                        request_json = await request.json()
                        handler_kwargs[name] = param.annotation(**request_json)
                    except ValidationError as e:
                        raise HttpValidationError(e.errors())
                
                # dependency injection logic.
                elif isinstance(param.default, Depends):
                    # Resolve `Depends` dependencies
                    dep_func = param.default.dependency
                    dep_sig = inspect.signature(dep_func)
                    sub_dep_kwargs = {}
                    if 'request' in dep_sig.parameters:
                        sub_dep_kwargs['request'] = request
                    if 'db' in dep_sig.parameters:
                        sub_dep_kwargs['db'] = db_session
                    handler_kwargs[name] = await dep_func(**sub_dep_kwargs)

            # --- Call the Handler ---
            if asyncio.iscoroutinefunction(handler):
                result = await handler(**handler_kwargs)
            else:
                result = handler(**handler_kwargs)
            
            # --- Prepare the Response ---
            if isinstance(result, Response): response = result
            else: response = JsonResponse(result)

        # --- Exception Handling ---
        except HttpValidationError as e: response = JsonResponse({"detail": e.errors}, status_code=422)
        except AuthenticationError: response = JsonResponse({"error": "Authentication required"}, status_code=401)
        except FileNotFoundError:
            if 404 in self.error_handlers:
                template = self.template_env.get_template(self.error_handlers[404])
                html_content = template.render(path=scope.get("path", "unknown"))
                response = Response(html_content, status_code=404)
            else:
                response = Response("<h1>404 Not Found</h1>", status_code=404)
        except MethodNotAllowedError:
            if 405 in self.error_handlers:
                template = self.template_env.get_template(self.error_handlers[405])
                html_content = template.render(path=scope.get("path", "unknown"), method=scope.get("method"))
                response = Response(html_content, status_code=405)
            else:
                response = Response("<h1>405 Method Not Allowed</h1>", status_code=405)
        except Exception as e:
            log.exception(f"Unhandled exception on path {scope.get('path')}")
            if 500 in self.error_handlers:
                template = self.template_env.get_template(self.error_handlers[500])
                html_content = template.render(path=scope.get("path", "unknown"), error=e)
                response = Response(html_content, status_code=500)
            else:
                response = Response("<h1>500 Internal Server Error</h1>", status_code=500)
        finally:
            # Ensure the database session is always closed.
            await db_session.close()

        await response(scope, receive, send)

    def find_handler(self, path, method):
        """
        Finds a matching route handler for a given path and method.

        Args:
            path: The request path.
            method: The request HTTP method.

        Returns:
            A tuple of (handler_function, path_parameters_dict).

        Raises:
            FileNotFoundError: If no route matches the path.
            MethodNotAllowedError: If a route matches the path but not the method.
        """
        path_found = False
        for route in self.routes:
            # Convert path format like "/users/{id:int}" to a regex
            pattern = "^" + re.sub(r'\{(\w+)(?::\w+)?\}', r'(?P<\1>[^/]+)', route.path) + "$"
            match = re.match(pattern, path)
            
            if match:
                path_found = True
                if method in route.methods:
                    return route.handler, match.groupdict()
        
        if path_found:
            raise MethodNotAllowedError()
        raise FileNotFoundError()

    def run(self, host='127.0.0.1', port=8000):
        """
        Runs the application using the Uvicorn server.

        Before starting the server, this method automatically calls `model_rebuild()`
        on all generated Pydantic schemas. This is a crucial step that resolves
        any forward references in models with circular dependencies (e.g., User -> Post -> User),
        preventing `PydanticUserError` at runtime.

        Args:
            host: The host to bind to.
            port: The port to bind to.
        """
        # Import here to avoid circular dependency issues at module load time.
        from .orm import _model_registry
        for model in _model_registry:
            if hasattr(model, '__pydantic_read_model__'):
                model.__pydantic_read_model__.model_rebuild()
            if hasattr(model, '__pydantic_create_model__'):
                model.__pydantic_create_model__.model_rebuild()

        print(f"🚀 Jetio server running on http://{host}:{port}")
        uvicorn.run(self, host=host, port=port)

class Route:
    """Represents a single route in the application."""
    def __init__(self, path, handler, methods):
        """
        Initializes a Route object.

        Args:
            path: The URL path string.
            handler: The view function to handle requests for this route.
            methods: A list of allowed HTTP methods.
        """
        self.path, self.handler, self.methods = path, handler, methods