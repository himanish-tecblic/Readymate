from rest_framework import serializers
from .models import *
from rest_framework import status



class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request

      class Meta:
        model = User
        fields=['email', 'name', 'password', 'phone']

      def validate(self, attrs):
        return attrs
      def create(self,validate_data):
        return User.objects.create(**validate_data)  
  
  
  
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

