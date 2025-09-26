"""
Jetio: A modern, high-performance Python web framework.

This file serves as the main entry point for the Jetio framework,
re-exporting key components from various modules to provide a simple
and unified public API for developers.
"""

__version__ = "1.0.3"

from .framework import Jetio, Request, Response, JsonResponse, BaseMiddleware

# Re-export Starlette's UploadFile for developer convenience
from starlette.datastructures import UploadFile

# Import from the new middleware module
from .middleware import CORSMiddleware

# Import from the config module
from .config import settings

# Import from the ORM module
from .orm import JetioModel, Base, engine, SessionLocal, relationship

# Import from the auth module
from .auth import verify_password, get_password_hash, create_access_token, decode_access_token

# Import from the openapi module
from .openapi import add_swagger_ui

# Import from the crud module
from .crud import CrudRouter

# Import ValidationError directly from the Pydantic library
from pydantic import ValidationError
