"""
URLS.PY — El enrutador principal.

Piénsalo como una tabla de contenido:
  /admin/           → panel de administración de Django
  /api/usuarios/    → API de usuarios inscritos
  /api/galeria/     → API de fotos/videos
  /api/links/       → API de recursos y links
  /media/           → archivos subidos (fotos)
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Panel admin de Django — entra con superusuario
    path('admin/', admin.site.urls),

    # Nuestras APIs — cada app tiene su propio urls.py
    path('api/usuarios/', include('usuarios.urls')),
    path('api/galeria/',  include('galeria.urls')),
    path('api/links/',    include('links.urls')),
]

# En desarrollo, Django sirve los archivos de media (fotos subidas)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
