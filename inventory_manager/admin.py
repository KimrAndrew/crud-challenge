from django.contrib import admin

from inventory_manager.models.Base_Entity import Base_Entity
from inventory_manager.models.Base_Inventory_Item import Base_Inventory_Item
from inventory_manager.models.Manufacturer import Manufacturer

# Register your models here.
admin.register(Base_Entity,Base_Inventory_Item, Manufacturer)