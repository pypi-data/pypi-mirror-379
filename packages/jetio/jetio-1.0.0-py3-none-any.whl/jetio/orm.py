"""
Object-Relational Mapping (ORM) utilities for the Jetio framework.

This module provides the foundation for database interaction in Jetio. It includes:
- A SQLAlchemy async engine and session setup.
- A declarative base class (`Base`) for model definitions.
- A custom `JetioModel` base class with a metaclass that automatically
  generates Pydantic schemas (`CreateSchema`, `ReadSchema`) from SQLAlchemy
  model definitions. This significantly reduces boilerplate code for developers.
"""

import inspect
import sys
from enum import Enum
from datetime import date, datetime
from sqlalchemy import inspect as sa_inspect
from typing import List, Any, Union, get_origin, get_args, ForwardRef, Optional
from pydantic import create_model, ConfigDict
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    sessionmaker, declarative_base, relationship as sa_relationship, Relationship,
    Mapped, mapped_column, ColumnProperty, InstrumentedAttribute
)

from .config import settings

# --- Core Database and ORM Setup ---
engine = create_async_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()
_model_registry = [] # A registry to keep track of all defined models for OpenAPI generation.

# --- Helper Functions ---
def relationship(*args, **kwargs) -> Relationship:
    """A simple wrapper around SQLAlchemy's relationship to provide a consistent API."""
    return sa_relationship(*args, **kwargs)

# --- The Metaclass that Builds Other Classes ---
class ModelMetaclass(type(Base)):
    """
    A metaclass that automatically generates Pydantic models from SQLAlchemy models.

    For each SQLAlchemy model that inherits from `JetioModel`, this metaclass
    introspects its columns and relationships to create two Pydantic models:
    - `ModelNameRead`: For serializing data (API responses).
    - `ModelNameCreate`: For validating data (API request bodies).

    This automation simplifies API development by ensuring that data validation
    and serialization schemas are always in sync with the the database model.
    """
    def __new__(cls, name, bases, attrs):
        # __new__ is responsible for creating the class object.
        # We can modify the class attributes here before the class is created.
        
        # If a tablename isn't provided and the class isn't abstract,
        # create a default one based on the class name (e.g., 'Minister' -> 'ministers').
        if '__tablename__' not in attrs and not attrs.get('__abstract__', False):
            attrs['__tablename__'] = name.lower() + 's'
            
        # __new__ is responsible for creating the class object.
        # We let the parent metaclass (from SQLAlchemy's declarative_base) do its work.
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        # __init__ is called after the class object `cls` has been created.
        # This is a safer place to perform inspection and modification.
        super().__init__(name, bases, attrs)
        
        if attrs.get('__abstract__', False):
            return

        # Collect all annotations from the class hierarchy.
        all_annotations = {}
        for base in cls.__mro__:
            if base is Base:
                break
            all_annotations = {**getattr(base, '__annotations__', {}), **all_annotations}

        pydantic_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
        api_config = attrs.get('API')
        exclude_from_read = getattr(api_config, 'exclude_from_read', [])

        def get_python_type_from_mapped(mapped_type):
            """Extracts the Python type from a SQLAlchemy `Mapped` annotation."""
            if get_origin(mapped_type) is Mapped:
                return get_args(mapped_type)[0]
            return mapped_type

        def resolve_pydantic_type(typ):
            """Resolves a SQLAlchemy type to a Pydantic-compatible type for the Read schema."""
            typ = get_python_type_from_mapped(typ)
            origin = get_origin(typ)

            # Handle Optional[T], which is represented as Union[T, None]
            if origin is Union:
                args = get_args(typ)
                non_none_args = [t for t in args if t is not type(None)]
                if len(non_none_args) == 1:
                    inner_type = non_none_args[0]
                    # Check if the inner type is a relationship that needs forward referencing.
                    is_relationship = (
                        isinstance(inner_type, ForwardRef) or
                        (inspect.isclass(inner_type) and issubclass(inner_type, JetioModel))
                    )
                    if is_relationship:
                        # Recursively resolve the inner type (e.g., "QuestionCategory" -> "QuestionCategoryRead")
                        resolved_inner_type = resolve_pydantic_type(inner_type)
                        # Reconstruct as Optional[ForwardRef('...Read')] to handle circular dependencies.
                        return Optional[ForwardRef(str(resolved_inner_type))]
                    # For simple optionals like Optional[int], just return the original type.
                    return typ

            if isinstance(typ, ForwardRef):
                return f'{typ.__forward_arg__}Read'
            if isinstance(typ, str):
                return f'{typ}Read'
            if inspect.isclass(typ) and issubclass(typ, JetioModel):
                return f'{typ.__name__}Read'
            return typ

        # --- Generate Read Schema ---
        read_fields = {}

        for field_name, field_type in all_annotations.items():
            if field_name.startswith('_') or field_name in exclude_from_read:
                continue

            python_type = get_python_type_from_mapped(field_type)
            origin = get_origin(python_type)

            # To prevent circular dependencies in API responses, we adopt a simple convention:
            # any relationship that is a list (i.e., a "to-many" relationship) is excluded
            # from the serialization schema. This is the safest and most common pattern.
            if origin is list or origin is List:
                continue

            final_type = resolve_pydantic_type(python_type)
            read_fields[field_name] = (final_type, None)

        # --- Generate Create Schema ---
        create_fields = {}
        # Fields that are typically managed by the server or database.
        server_side_fields = {'id', 'created_at', 'updated_at', 'hashed_password', 'password_hash', 'url_slug'}
        for k, v in all_annotations.items():
            attr_value = None
            for base in cls.__mro__:
                if k in base.__dict__:
                    attr_value = base.__dict__[k]
                    break
            
            has_server_default = hasattr(attr_value, 'default') and attr_value.default is not None

            # This is the robust way to detect a relationship field. It handles direct
            # class references (e.g., `Mapped[User]`) and forward references (e.g., `Mapped["User"]`)
            # for both to-one and to-many relationships.
            is_relationship = False
            py_type_for_check = get_python_type_from_mapped(v)
            type_origin = get_origin(py_type_for_check)
            type_args = get_args(py_type_for_check)

            # Determine the core type to inspect for a relationship.
            # This handles List[T] and Optional[T] (which is Union[T, None]).
            core_type = None
            if type_origin in (list, List) and type_args:
                core_type = type_args[0]
            elif type_origin is Union and type_args:
                # Find the first non-None type in the Union for Optional[T]
                non_none_args = [t for t in type_args if t is not type(None)]
                if len(non_none_args) == 1:
                    core_type = non_none_args[0]
            else:
                core_type = py_type_for_check

            if core_type and (isinstance(core_type, ForwardRef) or (inspect.isclass(core_type) and issubclass(core_type, JetioModel))):
                is_relationship = True

            # Include fields in the create schema if they are not server-managed
            # and are not relationships.
            # 💡 FIX IS HERE: The overly aggressive `is_managed_foreign_key` check has been removed. Note to future contributors
            # This will now include fields like `creator_id` in the CreateSchema, allowing
            # developers to pass them in the payload for non-secure routes.
            if not k.startswith('_') and k not in server_side_fields and not has_server_default and not is_relationship:
                 python_type = get_python_type_from_mapped(v)
                 is_optional = get_origin(python_type) is Union and type(None) in get_args(python_type)
                 if is_optional:
                     create_fields[k] = (python_type, None)
                 else:
                     create_fields[k] = (python_type, ...)

        # Create and attach the Pydantic models to the SQLAlchemy model's module.
        module = sys.modules[cls.__module__]
        pydantic_read_model = create_model(
            f"{name}Read", 
            **read_fields, 
            __config__=pydantic_config,
            __module__=module.__name__
        )
        pydantic_create_model = create_model(
            f"{name}Create", 
            **create_fields, 
            __config__=pydantic_config,
            __module__=module.__name__
        )
        
        setattr(module, pydantic_read_model.__name__, pydantic_read_model)
        setattr(module, pydantic_create_model.__name__, pydantic_create_model)
        
        # Attach the Pydantic models directly to the SQLAlchemy class for easy access.
        setattr(cls, '__pydantic_read_model__', pydantic_read_model)
        setattr(cls, '__pydantic_create_model__', pydantic_create_model)

        # Add the new model to the registry for OpenAPI generation.
        if cls not in _model_registry:
            _model_registry.append(cls)

# --- The Base Class for Developers ---
class JetioModel(Base, metaclass=ModelMetaclass):
    """
    The base model for all database tables in a Jetio application.
 
    By inheriting from this class, your SQLAlchemy models will automatically
    get Pydantic schemas generated for them, which can be used for API
    validation and serialization.
    """
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)

    def to_dict(self):
        """
        Serializes the SQLAlchemy model instance to a dictionary using its
        auto-generated Pydantic Read schema.
        """
        return self.__pydantic_read_model__.from_orm(self).model_dump()