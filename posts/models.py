from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Basic blog post entity."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
