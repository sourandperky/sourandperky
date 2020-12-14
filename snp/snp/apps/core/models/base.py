from base64 import urlsafe_b64decode, urlsafe_b64encode
from uuid import UUID, uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_lifecycle import BEFORE_CREATE, LifecycleModel, hook
from simple_history.models import HistoricalRecords


class Base(LifecycleModel):
    id = models.UUIDField(primary_key=True, db_index=True, editable=False, default=uuid4, verbose_name=_("ID"))
    slug = models.SlugField(db_index=True, null=True, blank=True, verbose_name=_("Slug"))
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name=_("Updated At"))

    @hook(BEFORE_CREATE)
    def create_slug_from_id(self):
        # We want to use the slug in the urls, so we are adding them to the database for ease of access
        # It might also make sense to create slug field and this hook in another mixin but I don't see
        # the harm in creating a slug for every database object, we will be using this model even in m2m through tables
        # which would allow us to serve the through models as activity in the users profile
        # We would preferably switch this guy into a generated field in postgres as soon as django supports it
        # instead of writing this inside a hook on application logic
        self.slug = self._uuid2slug(self.id)

    history = HistoricalRecords(inherit=True)

    @staticmethod
    def _uuid2slug(uuid):
        return urlsafe_b64encode(uuid.bytes).rstrip(b"=").decode("ascii")

    @staticmethod
    def _slug2uuid(slug):
        return UUID(bytes=urlsafe_b64decode(slug + "=="))

    class Meta:
        abstract = True
