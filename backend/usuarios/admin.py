"""
ADMIN.PY

Aquí registras tus modelos para que aparezcan en /admin/
Puedes personalizar muchísimo cómo se ven y qué puedes hacer.
"""
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    # Columnas que se muestran en la lista
    list_display  = ['nombre', 'apellido', 'email', 'programa', 'fecha_registro', 'activo']

    # Filtros en la barra lateral derecha
    list_filter   = ['programa', 'edad', 'fuente', 'activo']

    # Barra de búsqueda
    search_fields = ['nombre', 'apellido', 'email']

    # Campos que se pueden editar directo en la lista (sin entrar al detalle)
    list_editable  = ['activo']

    # Orden por defecto
    ordering = ['-fecha_registro']

    # Cómo se agrupan los campos en el formulario de detalle
    fieldsets = (
        ('Información personal', {
            'fields': ('nombre', 'apellido', 'email', 'telefono', 'edad')
        }),
        ('Inscripción', {
            'fields': ('programa', 'fuente', 'mensaje')
        }),
        ('Estado', {
            'fields': ('activo', 'fecha_registro'),
        }),
    )
    readonly_fields = ['fecha_registro']
