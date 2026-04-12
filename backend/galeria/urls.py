from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemGaleriaViewSet

router = DefaultRouter()
router.register(r'', ItemGaleriaViewSet, basename='galeria')
urlpatterns = [path('', include(router.urls))]
