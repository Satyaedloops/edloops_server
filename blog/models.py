from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
import uuid

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Add a random string to the slug
            self.slug += '-' + get_random_string(length=6)
        super().save(*args, **kwargs)