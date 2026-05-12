from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InsumosViewSet

router = DefaultRouter()
router.register(r'insumos', InsumosViewSet, basename='insumo')

urlpatterns = [
  path('', include(router.urls)),
]