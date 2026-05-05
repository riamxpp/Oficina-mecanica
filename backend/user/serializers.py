from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    # Tornamos a senha 'write_only' para que ela NUNCA seja retornada na resposta da API
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')

    def create(self, validated_data):
        # O método create_user do ORM do Django já faz o hash (criptografia) da senha automaticamente
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            is_staff=validated_data.get('is_staff', False),
        )
        return user