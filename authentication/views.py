import jwt

from django.conf import settings
from django.contrib import auth
from rest_framework.generics import GenericAPIView
from rest_framework import status, response
from authentication.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
)


class RegisterAPiView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if not user:
            return response.Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        auth_token = jwt.encode(
            {'username':user.username},
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        user_data = UserSerializer(user).data
        user_data['token'] = auth_token
        return response.Response(user_data, status=status.HTTP_200_OK)
