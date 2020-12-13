from django.contrib.auth.models import AbstractUser

from .base import Base


class User(AbstractUser, Base):
    ...
