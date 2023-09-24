from django.db import models
from django.utils import timezone
from user_api.models import User
import uuid


class BlogPost(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )

    title = models.CharField(
        max_length=140,
        null=False,
        blank=True
    )

    subtitle = models.CharField(
        max_length=140,
        null=False,
        blank=True
    )

    content = models.CharField(
        max_length=5000,
        null=False,
        blank=True
    )

    published = models.DateTimeField(
        null=False,
        blank=False,
        default=timezone.now
    )

    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, null=True)

    deleted = models.BooleanField(
        null=False,
        default=False
    )

    def __str__(self):
        return self.content


class Keyword(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )

    blog_post = models.ForeignKey(BlogPost, related_name="keywords", on_delete=models.CASCADE)

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
