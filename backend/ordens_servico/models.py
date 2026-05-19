from django.db import models
from veiculos.models import Veiculo
from core.models import Procedimento, Insumo

class OrdemServico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='ordens_servico')
    data_abertura = models.DateTimeField(auto_now_add=True)
    procedimentos = models.ManyToManyField(Procedimento, blank=True)
    
    def __str__(self):
        return f"OS #{self.id} - {self.veiculo.placa} ({self.get_status_display()})"