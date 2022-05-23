from django.db import models


class WarehouseManager(models.Manager):
    def get_queryset(self):
        return WarehouseQuerySet(self.model, using=self._db)

class Warehouse(models.Model):
    location = models.CharField(max_length=32)
    
    def __str__(self):
        return self.location
    
    def get_inventory(self):
        return 

class WarehouseQuerySet(models.QuerySet):

    # def inventory(self,warehouse:Warehouse):
    #     return WarehouseItem.items.filter(warehouse_id=warehouse.id)
    pass




    # def request_item(self, requested_quantity:int):
    #     if self.item.quantity >= requested_quantity:
    #         self.item.quantity -= requested_quantity
    #         self.warehouse_inventory += requested_quantity
    #     else:
    #         raise ValueError(
    #             f"Not Enough {self.item.name} in stock. Requested: {requested_quantity} {self.item.name}")

    # def return_item(self, returned_amount:int):
    #     if self.warehouse_inventory >= returned_amount:
    #         self.warehouse_inventory -= returned_amount
    #         self.item.quantity += returned_amount
    #     else:
    #         raise ValueError(
    #             f"Not Enough {self.item.name} in stock. Requested: {returned_amount}"
    #         )
    # def sell_item(self, amount_sold:int):
    #     if self.warehouse_inventory >= amount_sold:
    #         self.warehouse_inventory -= amount_sold
    #     else:
    #         raise ValueError(
    #             f"Not Enought {self.item.name} in stock. Requested: {amount_sold}"
    #         )