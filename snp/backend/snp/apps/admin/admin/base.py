from admin_auto_filters.filters import AutocompleteFilterFactory as Autocomplete
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy as _
from utils import with_attrs


class BaseAdmin(ModelAdmin):
    annotated_fields = []
    fieldsets_initial = []
    base_readonly_fields = [
        "id",
        "slug",  # We probably are gonna change this with something like "universal_slug" in the models
        "created_at",
        "updated_at",
    ]
    base_search_fields = ["id"]

    @staticmethod
    def make_fieldset_field(*fields, name=None):
        return (
            name and _(name),
            {
                "fields": fields,
            },
        )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        _type = type(fieldsets)

        fieldsets = [
            self.make_fieldset_field("id", "slug", "created_at", "updated_at", name="Meta"),
        ]

        if self.fieldsets_initial:
            fieldsets.insert(0, self.make_fieldset_field(*self.fieldsets_initial))
        return _type(fieldsets)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj=obj)
        return type(readonly_fields)([*self.base_readonly_fields, *readonly_fields])

    def get_list_filter(self, request):
        list_filter = super().get_list_filter(request)
        return type(list_filter)(
            [Autocomplete(_(f.title()), f) if f in self.autocomplete_fields else f for f in list_filter]
        )

    def get_search_fields(self, request):
        search_fields = super().get_search_fields(request)
        return type(search_fields)([*self.base_search_fields, *search_fields])

    @classmethod
    def _create_annotated_field_methods(cls):
        for field in cls.annotated_fields:

            @with_attrs(__name__=field, short_description=field)  # We probably don't want to set short_desc like this
            def attr_function(obj):
                return getattr(obj, field)

            setattr(cls, field, staticmethod(attr_function))

    def __init_subclass__(cls, **kwargs):
        cls._create_annotated_field_methods()

    class Media:
        """Necessary for django-admin-autocomplete-filters"""

        ...
