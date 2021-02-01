from apps.core.models import Topic
from django.contrib.admin import register

from .base import BaseAdmin


@register(Topic)
class TopicAdmin(BaseAdmin):
    fieldsets_initial = ["name"]
    search_fields = ["name"]
    autocomplete_fields = []
    list_display = ["name"]
    list_filter = []
