from rest_framework.serializers import ModelSerializer
from ..models.BasicProduct import BasicProduct

class BasicProductSerializer(ModelSerializer):
    class Meta:
        model = BasicProduct
        fields = '__all__'