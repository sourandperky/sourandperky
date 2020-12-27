from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import Base


class Topic(Base):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")
