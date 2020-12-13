from base64 import urlsafe_b64decode, urlsafe_b64encode
from uuid import UUID, uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name=_("ID"))
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name=_("Updated At"))

    history = HistoricalRecords(inherit=True)

    @staticmethod
    def _uuid2slug(uuid):
        return urlsafe_b64encode(uuid.bytes).rstrip(b"=").decode("ascii")

    @staticmethod
    def _slug2uuid(slug):
        return UUID(bytes=urlsafe_b64decode(slug + "=="))

    class Meta:
        abstract = True
