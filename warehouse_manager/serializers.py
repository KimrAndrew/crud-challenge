from rest_framework.serializers import ModelSerializer
from .models import WarehouseInventoryItem, Warehouse

class WarehouseInventoryItemSerializer(ModelSerializer):
    class meta:
        model = WarehouseInventoryItem
        fields = '__all__'

class WarehouseSerializer(ModelSerializer):
    class meta:
        model = Warehouse
        fields = '__all__'