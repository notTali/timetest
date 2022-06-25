import uuid
from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    role = models.TextField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name