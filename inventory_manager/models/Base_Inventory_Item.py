from django.db import models

class BaseInventoryItem(models.Model):
    """
    Fields:
    - name: str
    - description: str
    - price: int
    - quantity: int
    """
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    class Meta:
        abstract = True


