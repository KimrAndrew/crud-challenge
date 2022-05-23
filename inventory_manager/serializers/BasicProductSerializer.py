from rest_framework.serializers import ModelSerializer
from ..models.BaseProduct import BaseProduct

class BaseProductSerializer(ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = '__all__'