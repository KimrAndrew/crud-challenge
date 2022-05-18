from django.contrib import admin

from inventory_manager.models.Inventory_Item import InventoryItem


# Register your models here.
admin.site.register([InventoryItem])