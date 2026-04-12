from rest_framework import viewsets, permissions
from .models import ItemGaleria
from .serializers import ItemGaleriaSerializer

class ItemGaleriaViewSet(viewsets.ModelViewSet):
    serializer_class = ItemGaleriaSerializer

    def get_queryset(self):
        qs = ItemGaleria.objects.filter(activo=True)
        # Filtrar por tipo: /api/galeria/?tipo=foto
        tipo = self.request.query_params.get('tipo')
        if tipo:
            qs = qs.filter(tipo=tipo)
        return qs

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
