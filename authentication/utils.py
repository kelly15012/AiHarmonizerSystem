# authentication/utils.py
from django.contrib.auth.models import Group

def user_is_basic_or_pro(user):
    return user.groups.filter(name__in=['Basic', 'Pro']).exists()
