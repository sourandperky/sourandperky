from apps.core.models import Entry
from django.contrib.admin import register

from .base import BaseAdmin


@register(Entry)
class EntryAdmin(BaseAdmin):
    fieldsets_initial = ["title", "author", "content"]
    search_fields = ["content", "title", "id"]
    autocomplete_fields = ["author", "title"]
    list_display = ["title", "author", "created_at", "updated_at"]
    list_filter = ["author", "title"]
