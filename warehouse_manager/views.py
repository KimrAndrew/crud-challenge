from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import WarehouseInventoryItem, Warehouse

class Warehouse_Item_Detail(RetrieveUpdateDestroyAPIView):
    queryset = WarehouseInventoryItem.objects.all()
    serializer_class=WarehouseInventoryItemSerializer

class Warehouse_Item_List(ListCreateAPIView):
    queryset = WarehouseInventoryItem.objects.all()
    serializer_class = WarehouseInventoryItemSerializer

class Warehouse_List(ListCreateAPiView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class Warehouse_detail(RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer