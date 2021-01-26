import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_auth import relay

from .types import Entry, Title, Topic, User


class Query(graphene.ObjectType):
    """Queries specific to snp app."""

    user = graphene.relay.Node.Field(User)
    users = DjangoFilterConnectionField(User)
    entry = graphene.relay.Node.Field(Entry)
    entries = DjangoFilterConnectionField(Entry)
    title = graphene.relay.Node.Field(Title)
    titles = DjangoFilterConnectionField(Title)
    topic = graphene.relay.Node.Field(Topic)
    topics = DjangoFilterConnectionField(Topic)


class Mutation(graphene.ObjectType):
    """Mutations specific to snp app."""

    register = relay.Register.Field()
    verify_account = relay.VerifyAccount.Field()
    resend_activation_email = relay.ResendActivationEmail.Field()
    send_password_reset_email = relay.SendPasswordResetEmail.Field()
    password_reset = relay.PasswordReset.Field()
    password_set = relay.PasswordSet.Field()
    password_change = relay.PasswordChange.Field()
    update_account = relay.UpdateAccount.Field()
    archive_account = relay.ArchiveAccount.Field()
    delete_account = relay.DeleteAccount.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)  # NOQA  # No idea why does query screams like that.
