from rest_framework import serializers
from .models import ItemGaleria

class ItemGaleriaSerializer(serializers.ModelSerializer):
    # SerializerMethodField permite agregar campos calculados
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model  = ItemGaleria
        fields = ['id','tipo','titulo','descripcion','imagen','imagen_url','url_video','activo','fecha','orden']
        read_only_fields = ['id','fecha','imagen_url']

    def get_imagen_url(self, obj):
        """Devuelve la URL completa de la imagen incluyendo el dominio."""
        if obj.imagen:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.imagen.url)
        return None
