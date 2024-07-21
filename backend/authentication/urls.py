# backend/authentication/urls.py

from django.urls import path
from .views import UserCreate, AdminCreate, LoginCreate

urlpatterns = [
    path('register/user/', UserCreate.as_view(), name='register_user'),
    path('register/admin/', AdminCreate.as_view(), name='register_admin'),
    path('login/', LoginCreate.as_view(), name='login'),
]
