from apps.core.models import Topic as TopicModel

from .base import Base


class Topic(Base):
    class Meta:
        model = TopicModel
        fields = [
            "name",
            "titles",
        ]
        filter_fields = {
            "name": ["contains"],
        }
