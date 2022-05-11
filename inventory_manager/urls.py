from django.urls import path
from .views import Inventory_Item_Detail

urlpatterns = [
    path("",Inventory_Item_Detail.as_view(), name='inventory_item_detail'),
]