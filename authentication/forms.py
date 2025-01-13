from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment, Like, Profile, Feedback
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'media_url']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'required': True}),
            'media_url': forms.ClearableFileInput(attrs={'accept': 'image/*'})
        }

    def clean_media_url(self):
        media = self.cleaned_data.get('media_url', False)
        if media:
            if not media.content_type.startswith('image'):
                raise forms.ValidationError('Only image files are allowed.')
        return media

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2}),
        }

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['post', 'comment']
        widgets = {
            'post': forms.HiddenInput(),
            'comment': forms.HiddenInput(),
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            if not profile_picture.name.endswith(('.jpg', '.jpeg', '.png', '.webp')):
                raise ValidationError("Only .jpg, .jpeg, .png, and .webp files are allowed.")
        return profile_picture

class ContactForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']