from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import BaseFilterBackend

from .models import WarehouseInventoryItem, Warehouse
from .serializers import WarehouseInventoryItemSerializer, WarehouseSerializer

class Warehouse_Item_Detail(RetrieveUpdateDestroyAPIView):
    queryset = WarehouseInventoryItem.objects.all()
    serializer_class=WarehouseInventoryItemSerializer

class Warehouse_Item_List(APIView):
    def get(self,request,pk):
        warehouse = Warehouse.objects.filter(id=pk)[0]
        print(warehouse)
        inventory_queryset = WarehouseInventoryItem.objects.filter(warehouse=warehouse)
        serialized_inventory = WarehouseInventoryItemSerializer(inventory_queryset,many=True)
        return Response(serialized_inventory.data)

class Warehouse_List(ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class Warehouse_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer