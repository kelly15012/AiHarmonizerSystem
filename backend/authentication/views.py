# backend/authentication/views.py

from rest_framework import generics
from .models import User, Admin, Login
from .serializers import UserSerializer, AdminSerializer, LoginSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdminCreate(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class LoginCreate(generics.CreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
