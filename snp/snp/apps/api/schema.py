import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .mutations import Login, Logout
from .types import Entry, Title, Topic, User


class Query(graphene.ObjectType):
    """Queries specific to snp app."""

    users = DjangoFilterConnectionField(User)
    entries = DjangoFilterConnectionField(Entry)
    titles = DjangoFilterConnectionField(Title)
    topics = DjangoFilterConnectionField(Topic)


class Mutation(graphene.ObjectType):
    """Mutations specific to snp app."""

    login = Login.Field()
    logout = Logout.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
