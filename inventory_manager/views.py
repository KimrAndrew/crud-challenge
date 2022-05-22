from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from inventory_manager.models.BasicProduct import BasicProduct
from inventory_manager.serializers.BasicProductSerializer import BasicProductSerializer

# Create your views here.
class BasicProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = BasicProduct.objects.all()
    serializer_class=BasicProductSerializer

class BasicProductList(ListCreateAPIView):
    queryset = BasicProduct.objects.all()
    serializer_class = BasicProductSerializer