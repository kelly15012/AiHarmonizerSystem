from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscription/', views.subscription, name='subscription'),
    path('project/', views.project, name='project'),
    path('community/', views.community, name='community'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]
