from apps.core.models import Subscription
from django.contrib.admin import register

from .base import BaseAdmin


@register(Subscription)
class SubscriptionAdmin(BaseAdmin):
    fieldsets_initial = ["to", "by"]
    search_fields = ["to", "by"]
    autocomplete_fields = ["to", "by"]
    list_display = ["to", "by"]
    list_filter = ["to", "by"]
