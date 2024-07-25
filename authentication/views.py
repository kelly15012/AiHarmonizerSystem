from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        elif password != conpassword:
            messages.error(request, 'Passwords do not match')
        elif not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, 'Your account has been created successfully')
            return redirect('home') 

        return redirect('signup')
    
    return render(request, 'authentication/signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html',{'fname':fname})

        else:
            messages.error(request, 'Invalid credentials')
            return redirect('home')
        
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('home')

def subscription(request):
    return render(request, 'subscription.html')

def project(request):
    return render(request, 'project.html')

def community(request):
    return render(request, 'community.html')

def profile(request):
    return render(request, 'profile.html')