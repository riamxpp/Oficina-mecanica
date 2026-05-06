from django.db import models

class Cliente(models.Model):
    # RN01 - Preenchimento Obrigatório (blank=False, null=False por padrão no Django)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    endereco = models.TextField()
    telefone = models.CharField(max_length=20)
    
    # RN06 - Exclusão lógica para manter o histórico
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.nome
