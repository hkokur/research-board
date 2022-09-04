from django.db import models
from abstracts.models import (
    TimeStampedModel,
    UniqueizerModel,
    )
from django.conf import settings

class Board(UniqueizerModel, TimeStampedModel):
    """
    Base board model that every board have
    """
    description = models.CharField(max_length=1000)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="boards",
        related_query_name="board",
    )

    