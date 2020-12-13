from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .base import Base


class User(AbstractUser, Base):
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
