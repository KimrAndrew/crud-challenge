from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from inventory_manager.models.Inventory_Item import InventoryItem
from inventory_manager.serializers.inventory_item_serializer import Inventory_Item_Serializer

# Create your views here.
class Inventory_Item_Detail(RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class=Inventory_Item_Serializer

class Inventory_Item_List(ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = Inventory_Item_Serializer