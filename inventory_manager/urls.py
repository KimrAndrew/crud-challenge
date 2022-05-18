from django.urls import path
from .views import Inventory_Item_Detail, Inventory_Item_List

urlpatterns = [
    path("inventory_items/<int:pk>/",Inventory_Item_Detail.as_view(), name='inventory_item_detail'),
    path("inventory_items/",Inventory_Item_List.as_view(),name="inventory_item_list"),
]