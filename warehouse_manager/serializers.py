from rest_framework.serializers import ModelSerializer
from .models import WarehouseInventoryItem, Warehouse

class WarehouseInventoryItemSerializer(ModelSerializer):
    class Meta:
        model = WarehouseInventoryItem
        fields = '__all__'

class WarehouseSerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'