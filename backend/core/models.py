from django.db import models

# Create your models here.
class Insumos(models.Model):
  nome = models.CharField(max_length=255)
  marca = models.CharField(max_length=255)
  descricao = models.TextField()
  quantidade = models.FloatField(default=0.0)

  def __str__(self):
    return f"{self.nome} - {self.marca}"