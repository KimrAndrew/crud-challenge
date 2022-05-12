from rest_framework.serializers import ModelSerializer
from ..models.Inventory_Item import Inventory_Item

class Inventory_Item_Serializer(ModelSerializer):
    class Meta:
        model = Inventory_Item
        fiels = '__all__'