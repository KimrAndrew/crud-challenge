from rest_framework.views import APIView

# Create your views here.
class Inventory_Item_Detail(APIView):
    
    def post(self,request):
        print(request.data)