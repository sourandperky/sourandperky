from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import Base


class Vote(Base):
    """
    M2M between User and Entry for voting.
    """

    class TYPES(models.TextChoices):
        UP = "upvote", _("upvote")
        DOWN = "downvote", _("downvote")

    by = models.ForeignKey("User", on_delete=models.CASCADE)
    to = models.ForeignKey("Entry", on_delete=models.CASCADE)
    type = models.CharField(choices=TYPES.choices, max_length=10)

    class Meta:
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")
        constraints = [models.UniqueConstraint(fields=["by", "to"], name="unique_entry_vote")]
