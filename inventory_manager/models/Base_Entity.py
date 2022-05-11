from django.db import models

class Base_Entity(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        abstract = True