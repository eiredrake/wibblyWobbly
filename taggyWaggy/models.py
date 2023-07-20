from django.db import models
from tagging.fields import TagField
from tagging.registry import register


# Create your models here.
class Thingie(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    creator = models.CharField(blank=False, null=False, max_length=255)
    description = models.CharField(blank=False, null=False, max_length=255)

    tags = TagField()

    def __str__(self):
        return self.name
