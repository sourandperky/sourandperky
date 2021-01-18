from apps.core.models import User as UserModel

from .base import Base


class User(Base):
    class Meta:
        model = UserModel
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "email",
            "date_joined",
        ]
