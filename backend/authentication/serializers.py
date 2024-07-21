# backend/authentication/serializers.py

from rest_framework import serializers
from .models import User, Admin, Login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'fname', 'lname', 'gender', 'dob', 'email', 'createAt', 'modifiedAt']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['adminId', 'username', 'fname', 'lname', 'gender', 'email', 'lastLogin', 'createAt', 'modifiedAt']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['email', 'password', 'role', 'security_question_id', 'answer']
