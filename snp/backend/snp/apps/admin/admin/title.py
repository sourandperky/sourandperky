from apps.core.models import Title
from django.contrib.admin import register
from django.db.models import Count

from .base import BaseAdmin


@register(Title)
class TitleAdmin(BaseAdmin):
    fieldsets_initial = ["name", "topic"]
    search_fields = ["name"]
    autocomplete_fields = [
        "topic"
    ]  # Should we remove the one's we don't use, or keep them for the sake of consistency?
    list_display = ["name", "entry_count"]
    list_filter = []
    annotated_fields = ["entry_count"]

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(entry_count=Count("entries"))
