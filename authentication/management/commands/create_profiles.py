from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authentication.models import Profile
from django.conf import settings
from PIL import Image
import os

class Command(BaseCommand):
    help = 'Create profiles for existing users without a profile'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        default_image_path = os.path.join(settings.MEDIA_ROOT, 'default.jpeg')
        
        if not os.path.exists(default_image_path):
            self.stdout.write(self.style.ERROR(f"Default image not found at {default_image_path}"))
            return

        for user in users:
            if not hasattr(user, 'profile'):
                profile = Profile.objects.create(user=user)
                
                with open(default_image_path, 'rb') as f:
                    profile.profile_picture.save('default.jpeg', f, save=True)

                self.stdout.write(self.style.SUCCESS(f'Profile created for {user.username}'))
