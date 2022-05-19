from django.contrib import admin

from warehouse_manager.models import WarehouseInventoryItem,Warehouse

# Register your models here.
admin.site.register([Warehouse,WarehouseInventoryItem])