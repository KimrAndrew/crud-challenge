from django.db import models
from inventory_manager.models.Inventory_Item import InventoryItem

class Warehouse(models.Model):
    location = models.CharField(max_length=32)

class WarehouseInventoryItem(models.Model):
    warehouse = models.OneToOneField(Warehouse, on_delete=models.CASCADE)
    item = models.OneToOneField(InventoryItem, on_delete=models.CASCADE)
    warehouse_inventory = models.PositiveIntegerField(default=0)
    
    def request_item(self, requested_quantity:int):
        if self.item.quantity >= requested_quantity:
            self.item.quantity -= requested_quantity
            self.warehouse_inventory += requested_quantity
        else:
            raise ValueError(
                f"Not Enough {self.item.name} in stock. Requested: {requested_quantity} {self.item.name}")
    def return_item(self, returned_amount:int):
        if self.warehouse_inventory >= returned_amount:
            self.warehouse_inventory -= returned_amount
            self.item.quantity += returned_amount
        else:
            raise ValueError(
                f"Not Enough {self.item.name} in stock. Requested: {returned_amount}"
            )
    def sell_item(self, amount_sold:int):
        if self.warehouse_inventory >= amount_sold:
            self.warehouse_inventory -= amount_sold
        else:
            raise ValueError(
                f"Not Enought {self.item.name} in stock. Requested: {amount_sold}"
            )
        

