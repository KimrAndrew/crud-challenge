from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from inventory_manager.models.BaseProduct import BaseProduct
from inventory_manager.serializers.BasicProductSerializer import BaseProductSerializer

# Create your views here.
class BaseProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class=BaseProductSerializer

class BaseProductList(ListCreateAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = BaseProductSerializer