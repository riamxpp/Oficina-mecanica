from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Insumos
from .serializers import InsumosSerializer

# Create your views here.
class InsumosViewSet(viewsets.ModelViewSet):
  queryset = Insumos.objects.all()
  serializer_class = InsumosSerializer
  permission_classes = (IsAuthenticated,)