from rest_framework import serializers

from productos.models import Productos


class PoductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'