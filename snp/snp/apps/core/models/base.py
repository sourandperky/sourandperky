import uuid

from django.db import models
from simple_history.models import HistoricalRecords


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
