from django.urls import path

from warehouse_manager.models import WarehouseInventoryItem
from .views import Warehouse_Item_Detail,Warehouse_Item_List,Warehouse_List,Warehouse_Detail

urlpatterns = [
    path("<int:pk>/",Warehouse_Detail.as_view(), name='warehouse_detail'),
    path("",Warehouse_List.as_view(),name="warehouse_list"),
    path("<int:pk>/inventory/",Warehouse_Item_List.as_view(),name='warehouse_inventory')
]