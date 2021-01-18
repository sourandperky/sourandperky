import graphene
from django.contrib.auth import authenticate, login, logout

from ..types import User
from .base import Base


class Login(Base):
    """Authentication mutation, creates the session."""

    class Input:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    user = graphene.Field(User)

    @classmethod
    def mutate_and_get_payload(cls, root, info, username, password):
        """Log the user in."""
        user = authenticate(username=username, password=password)
        if user:
            login(info.context, user)
            payload = Login(success=True, user=user)
        else:
            payload = Login(success=False)
        return payload


class Logout(Base):
    """Authentication mutation."""

    success = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        """Log the user out from Django."""
        logout(info.context)
        return Logout(success=True)
