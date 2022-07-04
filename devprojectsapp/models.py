import uuid
from django.db import models

# Create your models here.
DEFAULT = 'default.jpeg'
class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, default=DEFAULT)
    role = models.TextField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name