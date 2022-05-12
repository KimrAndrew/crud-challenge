from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from inventory_manager.models.Inventory_Item import Inventory_Item
from inventory_manager.serializers.inventory_item_serializer import Inventory_Item_Serializer

# Create your views here.
class Inventory_Item_Detail(APIView):
    
    def post(self,request):
        print(request.data)

class Invetory_Item_List(ListCreateAPIView):
    queryset = Inventory_Item.objects.all()
    serializer = Inventory_Item_Serializer