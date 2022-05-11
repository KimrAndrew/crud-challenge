from django.db import models
from .Manufacturer import Manufacturer

class Base_Inventory_Item(models.Model):
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    class Meta:
        abstract = True


