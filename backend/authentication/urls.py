# backend/authentication/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscription/', views.subscription, name='subscription'),
    path('project/', views.project, name='project'),
    path('community/', views.community, name='community'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]