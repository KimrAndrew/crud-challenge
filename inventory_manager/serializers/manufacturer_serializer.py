from rest_framework.serializers import ModelSerializer

from ..models.Manufacturer import Manufacturer

class Manufacturer_Serializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'