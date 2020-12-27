from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import Base


class Title(Base):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Title")
        verbose_name_plural = _("Titles")
