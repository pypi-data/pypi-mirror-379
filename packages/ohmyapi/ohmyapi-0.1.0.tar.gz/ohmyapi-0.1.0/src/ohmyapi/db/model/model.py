from tortoise import fields
from tortoise.models import Model as TortoiseModel
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class Model(TortoiseModel):
    """
    Base Tortoise model with attached Pydantic schema generators via .Schema
    """

    class Schema:
        """
        Provides convenient access to auto-generated Pydantic schemas.
        """

        def __init__(self, model_cls):
            self.model_cls = model_cls

        @property
        def id(self):
            # Minimal schema with just the primary key field
            pk_field = self.model_cls._meta.pk_attr
            return pydantic_model_creator(
                self.model_cls, name=f"{self.model_cls.__name__}SchemaId", include=(pk_field,)
            )

        @property
        def get(self):
            # Full schema for reading
            return pydantic_model_creator(
                self.model_cls, name=f"{self.model_cls.__name__}SchemaGet"
            )

        @property
        def post(self):
            # Input schema for creation (no readonly fields like ID/PK)
            return pydantic_model_creator(
                self.model_cls,
                name=f"{self.model_cls.__name__}SchemaPost",
                exclude_readonly=True,
            )

        @property
        def put(self):
            # Input schema for updating
            return pydantic_model_creator(
                self.model_cls,
                name=f"{self.model_cls.__name__}SchemaPut",
                exclude_readonly=True,
            )

        @property
        def delete(self):
            # Schema for delete operations (just PK)
            pk_field = self.model_cls._meta.pk_attr
            return pydantic_model_creator(
                self.model_cls, name=f"{self.model_cls.__name__}SchemaDelete", include=(pk_field,)
            )

        @property
        def list(self):
            # Schema for list endpoints
            return pydantic_queryset_creator(self.model_cls)

        def from_fields(self, *fields: str):
            # Generate schema restricted to given fields
            valid = [f for f in fields if f in self.model_cls._meta.fields_map]
            return pydantic_model_creator(
                self.model_cls,
                name=f"{self.model_cls.__name__}SchemaFields",
                include=valid,
            )

    def __init_subclass__(cls, **kwargs):
        """
        Automatically attach .Schema to all subclasses
        """
        super().__init_subclass__(**kwargs)
        cls.Schema = cls.Schema(cls)

