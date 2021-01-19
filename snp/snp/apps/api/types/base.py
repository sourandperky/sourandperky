import graphene
from graphene_django import DjangoObjectType


class Base(DjangoObjectType):
    """GraphQL type for the {} model."""

    class Meta:
        abstract = True

    @staticmethod
    def _combine_meta(a, b):
        # No need to check the types with each other, this is an internal function anyway
        if isinstance(a, list):
            combined = a + b
        elif isinstance(a, dict):
            combined = {**a, **b}
        else:
            raise Exception
        return combined

    @classmethod
    def _read_from_base_meta(cls, attribute):
        # Add the Base fields
        if hasattr(cls.Meta, attribute):
            setattr(cls.Meta, attribute, cls._combine_meta(getattr(cls.Meta, attribute), getattr(cls._Meta, attribute)))
        else:
            setattr(cls.Meta, attribute, getattr(cls._Meta, attribute))

    def __init_subclass__(cls, **kwargs):
        # Create the description of the ObjectType automatically
        cls.__doc__ = Base.__doc__.format(cls.__name__)

        # Extend the subclass
        cls._read_from_base_meta("fields")
        cls._read_from_base_meta("filter_fields")
        cls._read_from_base_meta("interfaces")

        return super().__init_subclass__(**kwargs)

    class _Meta:
        fields = [
            "slug",
            "created_at",
            "updated_at",
        ]
        filter_fields = {"slug": ["exact"], "created_at": ["exact", "lt", "gt"], "updated_at": ["exact", "lt", "gt"]}
        interfaces = [
            graphene.relay.Node,
        ]
