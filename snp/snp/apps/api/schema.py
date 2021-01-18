import graphene

from .mutations import Login, Logout
from .types import Entry, Title, Topic, User


class Query(graphene.ObjectType):
    """Queries specific to snp app."""

    user = graphene.relay.Node.Field(User)
    entry = graphene.relay.Node.Field(Entry)
    title = graphene.relay.Node.Field(Title)
    topic = graphene.relay.Node.Field(Topic)


class Mutation(graphene.ObjectType):
    """Mutations specific to snp app."""

    login = Login.Field()
    logout = Logout.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
