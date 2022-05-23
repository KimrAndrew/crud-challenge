from django.urls import path

from warehouse_manager.models.WarehouseItem import WarehouseItem
from .views import Warehouse_Item_Detail,Warehouse_Item_List,Warehouse_List,Warehouse_Detail

urlpatterns = [
    path("<int:pk>/",Warehouse_Detail.as_view(), name='warehouse_detail'),
    path("",Warehouse_List.as_view(),name="warehouse_list"),
    path("inventory/<int:warehouse>/",Warehouse_Item_List.as_view(),name='warehouse_inventory'),
    path("inventory/<int:warehouse>/<int:pk>/",Warehouse_Item_Detail.as_view(),name="warehouse_item_detail")
]