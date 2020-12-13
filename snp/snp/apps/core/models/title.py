from django.utils.translation import gettext_lazy as _

from .base import Base


class Title(Base):
    class Meta:
        verbose_name = _("Title")
        verbose_name_plural = _("Titles")
