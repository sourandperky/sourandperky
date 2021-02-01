from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import Base


class Title(Base):
    REPR_FIELD = "name"

    name = models.CharField(max_length=100)
    topic = models.ForeignKey("core.Topic", on_delete=models.CASCADE, related_name="titles")

    class Meta:
        verbose_name = _("Title")
        verbose_name_plural = _("Titles")
