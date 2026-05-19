from rest_framework import viewsets
from .models import OrdemServico
from .serializers import OrdemServicoSerializer

class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer