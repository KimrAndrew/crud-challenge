from rest_framework.serializers import ModelSerializer
from ..models.Inventory_Item import InventoryItem

class Inventory_Item_Serializer(ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'