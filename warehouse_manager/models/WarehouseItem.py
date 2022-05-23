from django.db import models
from warehouse_manager.models.Warehouse import Warehouse
from inventory_manager.models.BaseProduct import BaseProduct

class WarehouseItemQuerySet(models.QuerySet):
    
    def allocated_products(self,product:BaseProduct) -> models.QuerySet:
        return WarehouseItem.items.filter(item__id = product.id)

    def product_quantity(self,product:BaseProduct):
        return self.allocated_products(product).aggregate(models.Sum('quantity'))

    def belonging_to(self,warehouse: Warehouse):
        return WarehouseItem.items.filter(warehouse__id=warehouse.id)

class WarehouseItemManager(models.Manager):

    def get_queryset(self):
        return WarehouseItemQuerySet(self.model, using=self._db)



class WarehouseItem(models.Model):

    warehouse = models.OneToOneField(Warehouse, on_delete=models.CASCADE)
    item = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    items = WarehouseItemQuerySet.as_manager()



