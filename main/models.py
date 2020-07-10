from django.db import models
from django.core import validators

# Create your models here.
class ShortenedURL(models.Model):
    name = models.SlugField(validators=[validators.MinLengthValidator(2)], unique=True)
    url = models.URLField(validators=[validators.URLValidator()])

    def __str__(self):
        return f"{self.name} ({self.url})"
