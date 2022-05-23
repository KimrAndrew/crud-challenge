from django.contrib import admin

from inventory_manager.models.BaseProduct import BaseProduct


# Register your models here.
admin.site.register([BaseProduct])