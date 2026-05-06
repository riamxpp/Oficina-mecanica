from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

# Create your tests here.
class UserCRUDTests(APITestCase):
  def setUp(self):
    self.user_data = { 
      'username': 'mecanico_chefe',
      'email': 'chefe@oficina.com',
      'password': 'senha_segura_123'
    }
    self.user = User.objects.create_user(**self.user_data) # cria um User teste no banco de testes.
    
    # Preparando as URLs nomeadas (baseadas no seu urls.py)
    self.register_url = reverse('register')
    self.user_detail_url = reverse('user_detail', kwargs={'pk': self.user.pk})

  def test_create_user(self): # cria e registra novo usuário
    novo_usuario = {
      'username': 'novo_ajudante',
      'email': 'ajudante@oficina.com',
      'password': 'senha_ajudante_123'
    }
    
    response = self.client.post(self.register_url, novo_usuario)
    
    self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Verifica se retornou 201 Created
    self.assertEqual(User.objects.count(), 2) # Agora temos 2 usuários no banco de testes (o criado no setUp e o novo)

  def test_read_user(self):
    self.client.force_authenticate(user=self.user) # Autentica o usuário criado no setUp
    
    response = self.client.get(self.user_detail_url)

    self.assertEqual(response.status_code, status.HTTP_200_OK) # Verifica se retornou 200 OK
    self.assertEqual(response.data['username'], self.user_data['username']) # Verifica se o username retornado é o correto
    self.assertNotIn('password', response.data) # Verifica se a senha não está sendo retornada
  
  def test_update_user(self):
    self.client.force_authenticate(user=self.user) # Autentica o usuário criado no setUp
    
    dados_atualizados = {
      'username': 'mecanico_chefe',
      'email': 'chefe_atualizado@oficina.com',
    }

    response = self.client.patch(self.user_detail_url, dados_atualizados)
    self.assertEqual(response.status_code, status.HTTP_200_OK) # Verifica se retornou 200 OK
    self.user.refresh_from_db() # Atualiza o objeto do banco de dados
    self.assertEqual(self.user.email, dados_atualizados['email']) # Verifica se o email foi atualizado corretamente