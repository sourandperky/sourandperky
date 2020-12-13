from django.utils.translation import gettext_lazy as _

from .base import Base


class Entry(Base):
    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")
