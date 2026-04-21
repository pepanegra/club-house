"""
MODELS.PY de usuarios

Un Model en Django es una clase Python que representa una tabla en la BD.
Cada atributo de la clase = una columna en la tabla.
Django hace la traducción a SQL automáticamente.
"""
from django.db import models

class Usuario(models.Model):
    """
    Representa a un joven que se inscribe al Club House.
    Django crea automáticamente un campo 'id' como clave primaria.
    """

    # CharField = texto corto (max_length es obligatorio)
    nombre   = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')

    # EmailField valida que el formato sea correcto (usuario@dominio.com)
    email    = models.EmailField(unique=True, verbose_name='Correo electrónico')

    # blank=True significa que el campo es opcional en formularios
    telefono = models.CharField(max_length=20, blank=True, verbose_name='Teléfono')

    EDAD_CHOICES = [
        ('10-13', '10 – 13 años'),
        ('14-17', '14 – 17 años'),
        ('18-22', '18 – 22 años'),
        ('23+',   '23 años o más'),
    ]
    edad = models.CharField(max_length=10, choices=EDAD_CHOICES, blank=True)

    PROGRAMA_CHOICES = [
        ('programacion',  'Programación'),
        ('robotica',      'Robótica'),
        ('iniciacion',    'Iniciación en tecnología'),
        ('diseno',        'Diseño 2D y 3D'),
        ('laboratorio',   'Laboratorio tecnológico'),
        ('saber_pacifico','Tecnología saber pacífico'),
        ('asesoria',      'Quiero asesoría'),
    ]
    programa = models.CharField(max_length=20, choices=PROGRAMA_CHOICES, blank=True, verbose_name='Programa de interés')

    FUENTE_CHOICES = [
        ('instagram',  'Instagram'),
        ('whatsapp',   'WhatsApp / amigo'),
        ('google',     'Google'),
        ('colegio',    'Colegio / universidad'),
        ('otro',       'Otro'),
    ]
    fuente = models.CharField(max_length=20, choices=FUENTE_CHOICES, blank=True, verbose_name='¿Cómo nos conoció?')

    # TextField = texto largo sin límite
    mensaje = models.TextField(blank=True, verbose_name='Mensaje')

    # BooleanField = verdadero o falso
    activo = models.BooleanField(default=True, verbose_name='Activo')

    # DateTimeField con auto_now_add=True guarda la fecha de creación automáticamente
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')

    class Meta:
        # Así se llama en el admin panel (singular y plural)
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        # Ordenar por fecha de registro, más reciente primero
        ordering = ['-fecha_registro']

    def __str__(self):
        # Esto define cómo se muestra el objeto en el admin y en el shell
        return f'{self.nombre} {self.apellido} — {self.email}'
