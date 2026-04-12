from django.contrib import admin
from .models import ItemGaleria

@admin.register(ItemGaleria)
class ItemGaleriaAdmin(admin.ModelAdmin):
    list_display  = ['titulo', 'tipo', 'activo', 'orden', 'fecha']
    list_filter   = ['tipo', 'activo']
    list_editable = ['activo', 'orden']
    search_fields = ['titulo', 'descripcion']
    ordering      = ['orden', '-fecha']
