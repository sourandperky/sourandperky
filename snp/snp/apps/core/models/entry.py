from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import Base


class Entry(Base):
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.ForeignKey("Title", on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")
