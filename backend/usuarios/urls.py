"""
URLS.PY de la app usuarios

El Router de DRF genera automáticamente todas las URLs del ViewSet.
Con estas 3 líneas obtienes:
  GET/POST   /api/usuarios/
  GET/PUT/DELETE /api/usuarios/{id}/
  GET        /api/usuarios/stats/
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
]
