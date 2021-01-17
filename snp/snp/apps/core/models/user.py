from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .base import Base
from .vote import Vote


class User(AbstractUser, Base):
    REPR_FIELD = "username"

    def down_vote(self, entry):
        return Vote.objects.create(entry=entry, user=self, type=Vote.TYPES.DOWN)

    def up_vote(self, entry):
        return Vote.objects.create(entry=entry, user=self, type=Vote.TYPES.DOWN)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
