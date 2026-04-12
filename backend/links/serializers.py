from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Link
        fields = ['id','titulo','url','descripcion','categoria','icono','activo','orden','fecha']
        read_only_fields = ['id','fecha']
