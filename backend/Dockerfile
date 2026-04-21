# Dockerfile — Le dice a Docker cómo construir el contenedor
#
# Imagínalo como una receta:
# 1. Parte de una imagen base (Python 3.11)
# 2. Copia tu código
# 3. Instala las dependencias
# 4. Arranca Django

# Imagen base — Python 3.11 en Linux ligero (slim)
FROM python:3.11-slim

# Evita que Python genere archivos .pyc innecesarios
ENV PYTHONDONTWRITEBYTECODE=1
# Hace que los logs aparezcan en tiempo real (importante para ver errores)
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Primero copia solo requirements.txt para aprovechar el cache de Docker
# (Si no cambia requirements.txt, no reinstala todo cada vez)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ahora copia todo el código
COPY . .

# Expone el puerto 8000 para que Django sea accesible
EXPOSE 8000

# Comando que se ejecuta al arrancar el contenedor
# En desarrollo usamos runserver, en producción usaríamos gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
