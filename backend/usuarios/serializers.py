"""
SERIALIZERS.PY

Un serializer convierte objetos Python (como un Usuario de la BD)
a JSON (para la API) y viceversa.

Es como un "traductor" entre tu base de datos y el mundo exterior.

Cuando el frontend hace GET /api/usuarios/ → el serializer convierte
los objetos Usuario a JSON.

Cuando el frontend hace POST /api/usuarios/ → el serializer valida
los datos JSON y los convierte a un objeto Usuario para guardar.
"""
from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    """
    ModelSerializer genera automáticamente los campos
    basándose en el modelo. Solo tienes que decirle qué campos incluir.
    """
    class Meta:
        model = Usuario
        fields = [
            'id', 'nombre', 'apellido', 'email',
            'telefono', 'edad', 'programa', 'fuente',
            'mensaje', 'activo', 'fecha_registro'
        ]
        # fecha_registro la pone Django automáticamente, no el usuario
        read_only_fields = ['id', 'fecha_registro']
