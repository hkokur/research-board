from django.db import models
import uuid
from abstracts.models import BaseCard


class UrlCard(BaseCard):
    note = models.TextField(blank=True, null=True)


class Url(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    url = models.URLField()
    card = models.ForeignKey(
        UrlCard,
        models.CASCADE,
        related_name="urls",
        related_query_name="url",
    )

    def __str__(self):
        return self.url