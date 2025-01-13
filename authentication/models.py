from django.db import models
from django.contrib.auth.models import User, Group
from PIL import Image

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    media_type = models.CharField(max_length=10, null=True, blank=True)  # e.g., 'image'
    media_url = models.ImageField(upload_to='posts/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post}'

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, related_name='likes', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Like by {self.user.username} on Post {self.post} or Comment {self.comment}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_plan = models.CharField(max_length=50, default='Free')
    profile_picture = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)

    def update_subscription(self, new_plan):
        # Remove user from all groups
        self.user.groups.clear()
        # Add user to the new plan group
        group, created = Group.objects.get_or_create(name=new_plan)
        self.user.groups.add(group)
        # Update the profile subscription plan
        self.subscription_plan = new_plan
        self.save()
    
class Chord(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.FloatField()
    duration = models.FloatField()
    # Add more fields as necessary

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name