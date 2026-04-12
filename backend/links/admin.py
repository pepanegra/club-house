from django.contrib import admin
from .models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display  = ['titulo', 'categoria', 'url', 'activo', 'orden']
    list_filter   = ['categoria', 'activo']
    list_editable = ['activo', 'orden']
    search_fields = ['titulo', 'url']
