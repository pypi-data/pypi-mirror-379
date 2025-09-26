from .framework import Response

class CORSMiddleware:
    """
    Handles Cross-Origin Resource Sharing (CORS) for the application.
    Allows frontends from different origins to communicate with the API.
    """
    def __init__(self, app, allowed_origins: list = None):
        self.app = app
        # Default to allowing all origins if none are specified
        self.allowed_origins = allowed_origins or ["*"]

    async def __call__(self, scope, receive, send):
        # Handle pre-flight OPTIONS requests
        if scope['method'] == 'OPTIONS':
            response = Response(status_code=200, content_type="text/plain", headers={
                "Access-Control-Allow-Origin": ", ".join(self.allowed_origins),
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Authorization, Content-Type",
            })
            await response(scope, receive, send)
            return

        # For actual requests, we need to add headers to the response
        async def send_with_cors_headers(message):
            if message['type'] == 'http.response.start':
                # Add CORS headers to the response
                headers = dict(message['headers'])
                headers[b"Access-Control-Allow-Origin"] = b", ".join(o.encode() for o in self.allowed_origins)
                message['headers'] = list(headers.items())
            await send(message)

        await self.app(scope, receive, send_with_cors_headers)
