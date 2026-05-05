from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # Permitir que qualquer pessoa acesse a rota de registro sem estar logada
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LogoutView(APIView):
  permission_classes = (IsAuthenticated,)

  def post(self, request):
    try:
      # PEGA O REFRESH DO FRONTEND E COLOCA-O EM UMA LISTA NEGRA.
      refresh_token = request.data["refresh"]
      token = RefreshToken(refresh_token)
      token.blacklist()

      return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
      return Response(status=status.HTTP_400_BAD_REQUEST)