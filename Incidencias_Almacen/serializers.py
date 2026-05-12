from rest_framework import serializers
from .models import Incidencia, Material, Proveedor, Operario

class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class OperarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operario
        fields = '__all__'