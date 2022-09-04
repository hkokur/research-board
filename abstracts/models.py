from django.db import models
import uuid
from django.utils.text import slugify


class UniqueizerModel(models.Model):
    """
    Uniqueize model with uuid and slug that generate from title 
    """
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, blank=True)
    
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) 
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating created and modified fields. 
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseCard(UniqueizerModel, TimeStampedModel):
    """
    Base model that every card have
    """
    boards = models.ManyToManyField(
        "boards.Board",
        related_name="%(class)ss",
        related_query_name="%(class)s",
    )

    class Meta:
        abstract = True


