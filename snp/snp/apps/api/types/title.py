from apps.core.models import Title as TitleModel

from .base import Base


class Title(Base):
    class Meta:
        model = TitleModel
        fields = [
            "name",
            "topic",
            "entries",
        ]
        filter_fields = {"name": ["contains"], "topic": ["exact"]}
