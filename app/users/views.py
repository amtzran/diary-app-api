from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from base.pagination import StandardResultsSetPagination
from base.response import *
from users.serializers import *


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(username=username, password=password)
        data = {'username': username, 'password': password}

        if user:
            login_serializer = self.serializer_class(data=data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)
                data = {
                    'access_token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'type': 'Bearer',
                    'user': user_serializer.data
                }
                return response_success(data=data, message='Bienvenido, sus credenciales son correctas.')
            return response_error(message='Las credenciales son incorrectas.')
        return response_error(message='Las credenciales son incorrectas.')


class Logout(GenericAPIView):
    @classmethod
    def post(cls, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return response_success(message='Sesión cerrada correctamente.')
        return response_not_found(message='No existe este usuario')
