from rest_framework import serializers
from .models import *
from rest_framework import status



class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request

  class Meta:
    model = User
    fields=['email', 'name', 'password', 'phone']
    extra_kwargs= {
      'password': {'write_only': True}
    }

  def validate(self, attrs):
    return attrs

