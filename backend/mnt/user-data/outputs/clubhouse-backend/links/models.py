from django.db import models

class Link(models.Model):
    CATEGORIA_CHOICES = [
        ('recurso',   'Recurso educativo'),
        ('comunidad', 'Comunidad'),
        ('herramienta','Herramienta'),
        ('documento', 'Documento'),
        ('otro',      'Otro'),
    ]
    titulo    = models.CharField(max_length=200)
    url       = models.URLField()
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='recurso')
    icono     = models.CharField(max_length=10, blank=True, help_text='Emoji del ícono, ej: 📚')
    activo    = models.BooleanField(default=True)
    orden     = models.PositiveIntegerField(default=0)
    fecha     = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = 'Link'
        verbose_name_plural = 'Links y recursos'
        ordering            = ['orden', '-fecha']

    def __str__(self):
        return f'{self.titulo} → {self.url}'
