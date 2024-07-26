from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscription/', views.subscription, name='subscription'),
    path('project/', views.project, name='project'),
    path('community/', views.community, name='community'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
