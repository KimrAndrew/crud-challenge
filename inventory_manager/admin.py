from django.contrib import admin

from inventory_manager.models.Base_Entity import Base_Entity
from inventory_manager.models.Base_Inventory_Item import Base_Inventory_Item
from inventory_manager.models.Inventory_Item import Inventory_Item
from inventory_manager.models.Manufacturer import Manufacturer
from inventory_manager.models.Customer import Customer
from inventory_manager.models.Merchant import Merchant

# Register your models here.
admin.register(Customer, Manufacturer, Inventory_Item,Merchant)