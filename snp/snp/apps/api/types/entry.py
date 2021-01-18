from apps.core.models import Entry as EntryModel

from .base import Base


class Entry(Base):
    class Meta:
        model = EntryModel
        fields = [
            "author",
            "title",
            "content",
        ]
