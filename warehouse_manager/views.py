from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import BaseFilterBackend

from .models import WarehouseInventoryItem, Warehouse
from inventory_manager.models.Inventory_Item import InventoryItem
from .serializers import WarehouseInventoryItemSerializer, WarehouseSerializer

class Warehouse_Item_Detail(RetrieveUpdateDestroyAPIView):
    queryset = WarehouseInventoryItem.objects.all()
    serializer_class=WarehouseInventoryItemSerializer

class Warehouse_Item_List(APIView):

    def _get_warehouse(self,warehouse):
        return Warehouse.objects.filter(id=warehouse)[0]

    def _get_global_item(self,item_id):
        return InventoryItem.objects.filter(id=item_id)
        
    def get(self,request,warehouse):
        warehouse = Warehouse.objects.filter(id=warehouse)[0]
        inventory_queryset = WarehouseInventoryItem.objects.filter(warehouse=warehouse)
        serialized_inventory = WarehouseInventoryItemSerializer(inventory_queryset,many=True)
        return Response(serialized_inventory.data)

    def put(self,request,warehouse):
        # get the warehouse whose inventory is being accessed
        warehouse= Warehouse.objects.filter(id=warehouse)[0]
        # get the global item being accessed
        item = InventoryItem.objects.filter(id=request.data.get("item"))[0]
        # add item to warehouse inventory or update if already present
        WarehouseInventoryItem.objects.update_or_create(warehouse=warehouse, item=item, defaults={'quantity':request.data.get('quantity')})
        return Response(request.data)

    # def delete(self,request,pk):
    #     warehouse = self._get_warehouse(pk)
    #     item = self._get_global_item(request.data.get("item")[0])

    #     item_to_delete = WarehouseInventoryItem.objects.get(warehouse=warehouse,item=item)
    #     WarehouseInventoryItem.objects.delete()



class Warehouse_List(ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class Warehouse_Detail(RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer