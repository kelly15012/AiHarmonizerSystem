# backend/authentication/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def subscription(request):
    return render(request, 'subscription.html')

def project(request):
    return render(request, 'project.html')

def community(request):
    return render(request, 'community.html')

def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')
