"""
VIEWS.PY

Las vistas son las funciones que reciben una petición HTTP y devuelven una respuesta.
Con Django REST Framework usamos 'ViewSets' que generan automáticamente
las operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

GET    /api/usuarios/      → lista todos los usuarios
POST   /api/usuarios/      → crea un usuario nuevo
GET    /api/usuarios/1/    → muestra el usuario con id=1
PUT    /api/usuarios/1/    → actualiza el usuario con id=1
DELETE /api/usuarios/1/    → elimina el usuario con id=1
"""
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet completo para usuarios.
    ModelViewSet nos da CRUD completo con muy poco código.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        """
        Permisos:
        - Cualquiera puede crear un usuario (inscribirse)
        - Solo admins pueden ver la lista, editar y eliminar
        """
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAdminUser])
    def stats(self, request):
        """
        Endpoint extra: /api/usuarios/stats/
        Devuelve estadísticas para el dashboard del admin.
        """
        total    = Usuario.objects.count()
        activos  = Usuario.objects.filter(activo=True).count()
        por_programa = {}
        for prog_code, prog_name in Usuario.PROGRAMA_CHOICES:
            count = Usuario.objects.filter(programa=prog_code).count()
            if count > 0:
                por_programa[prog_name] = count

        return Response({
            'total': total,
            'activos': activos,
            'por_programa': por_programa,
        })
