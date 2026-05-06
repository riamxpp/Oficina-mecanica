# serializers.py
from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'endereco', 'telefone', 'is_active']
        read_only_fields = ['id', 'is_active'] # Impede que o usuário altere o status de exclusão manualmente via API