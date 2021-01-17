from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import Base


class Subscription(Base):
    """
    M2M between User and Title for subscription.
    """

    by = models.ForeignKey("core.User", on_delete=models.CASCADE)
    to = models.ForeignKey("core.Title", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")
        constraints = [models.UniqueConstraint(fields=["by", "to"], name="unique_subscription")]
