from django.contrib import admin

from warehouse_manager.models.WarehouseItem import WarehouseItem
from warehouse_manager.models.Warehouse import Warehouse

# Register your models here.
admin.site.register([Warehouse,WarehouseItem])