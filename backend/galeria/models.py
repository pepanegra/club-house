from django.db import models

class ItemGaleria(models.Model):
    TIPO_CHOICES = [
        ('foto',  'Foto'),
        ('video', 'Video (YouTube)'),
    ]
    tipo        = models.CharField(max_length=10, choices=TIPO_CHOICES, default='foto')
    titulo      = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    # Para fotos: archivo subido
    imagen      = models.ImageField(upload_to='galeria/', blank=True, null=True)
    # Para videos: link de YouTube
    url_video   = models.URLField(blank=True)
    activo      = models.BooleanField(default=True)
    fecha       = models.DateTimeField(auto_now_add=True)
    orden       = models.PositiveIntegerField(default=0, help_text='Menor número = aparece primero')

    class Meta:
        verbose_name        = 'Item de galería'
        verbose_name_plural = 'Galería'
        ordering            = ['orden', '-fecha']

    def __str__(self):
        return f'[{self.tipo.upper()}] {self.titulo}'
