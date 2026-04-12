from rest_framework import viewsets, permissions
from .models import Link
from .serializers import LinkSerializer

class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        qs = Link.objects.filter(activo=True)
        categoria = self.request.query_params.get('categoria')
        if categoria:
            qs = qs.filter(categoria=categoria)
        return qs

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
