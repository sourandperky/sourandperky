from apps.core.models import User
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin


@register(User)
class UserAdmin(UserAdmin):
    search_fields = ["username"]
    autocomplete_fields = ["groups"]
    list_display = ["username", "first_name", "last_name", "is_active"]
    list_filter = ["is_active"]
