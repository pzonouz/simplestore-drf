from django.db import models
from core.models import TimeStampedUUID


class Category(TimeStampedUUID):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "categories"
