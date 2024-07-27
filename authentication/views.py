from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm, UserUpdateForm, ProfileUpdateForm

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
            messages.error(request, 'Username already exists', extra_tags='warning')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists', extra_tags='warning')
        elif password != conpassword:
            messages.error(request, 'Passwords do not match', extra_tags='warning')
        elif not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers', extra_tags='warning')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, 'Your account has been created successfully', extra_tags='success')
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
            messages.error(request, 'Invalid credentials', extra_tags='warning')
            return redirect('home')
        
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully', extra_tags='success')
    return redirect('home')

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        
        profile = user.profile
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        profile.save()
        
        user.save()
        messages.success(request, 'Your profile has been updated successfully', extra_tags='success')
        return redirect('profile')
    return render(request, 'authentication/profile.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!', extra_tags='success')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.', extra_tags='warning')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'authentication/change_password.html', {'form': form})

def subscription(request):
    return render(request, 'subscription.html')

def project(request):
    return render(request, 'project.html')

#Community
@login_required
def community(request):
    posts = Post.objects.all().order_by('-timestamp')
    for post in posts:
        post.user_has_liked = post.likes.filter(user=request.user).exists()
        for comment in post.comments.all():
            comment.user_has_liked = comment.likes.filter(user=request.user).exists()
    return render(request, 'authentication/community.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('community')

@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like, created = Like.objects.get_or_create(comment=comment, user=request.user)
    if not created:
        like.delete()
    return redirect('community')

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('community')
    else:
        form = CommentForm()
    return render(request, 'authentication/create_comment.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.media_type = 'image' if post.media_url else 'text'  # Set media_type based on media_url
            post.save()
            messages.success(request, 'Post created successfully.', extra_tags='success')
            return redirect('community')
        else:
            messages.error(request, 'There was an error creating your post.', extra_tags='warning')
    else:
        form = PostForm()
    return render(request, 'authentication/create_post.html', {'form': form})