import graphene
from graphene_django import DjangoObjectType


class Base(DjangoObjectType):
    """GraphQL type for the {} model."""

    class Meta:
        abstract = True

    def __init_subclass__(cls, **kwargs):
        # Create the description of the ObjectType automatically
        cls.__doc__ = Base.__doc__.format(cls.__name__)

        # Add the Base fields
        if hasattr(cls.Meta, "fields"):
            cls.Meta.fields[:0] = cls._Meta.fields
        else:
            cls.Meta.fields = cls._Meta.fields

        # Make every ObjectType a Relay Node
        if hasattr(cls.Meta, "interfaces"):
            cls.Meta.interfaces[:0] = cls._Meta.interfaces
        else:
            cls.Meta.interfaces = cls._Meta.interfaces

        return super().__init_subclass__(**kwargs)

    class _Meta:
        fields = [
            "id",
            "slug",
            "created_at",
            "updated_at",
        ]
        interfaces = [
            graphene.relay.Node,
        ]
