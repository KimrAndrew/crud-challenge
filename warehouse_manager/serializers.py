from rest_framework.serializers import ModelSerializer
from .models import WarehouseItem, Warehouse

class WarehouseItemSerializer(ModelSerializer):
    class Meta:
        model = WarehouseItem
        fields = '__all__'

class WarehouseSerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'