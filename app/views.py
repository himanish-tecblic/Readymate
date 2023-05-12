from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import UserRegistrationSerializer
from .serializers import UserLoginSerializer
import requests
from django.contrib.auth import authenticate

# Create your views here.



class UserRegistration(APIView):

    def post(self, request, *args, **kwargs):
        if request.data:
            data = request.data
            try:
                serializer = UserRegistrationSerializer(data=request.data)
                print("----------->>>>", serializer)
                if serializer.is_valid():
                    serializer.save()
                    email = serializer.validated_data['email']
                    phone = serializer.validated_data['phone']
                    user = User.objects.get(email=email)
                    print(user)

                    response = {
                        "success": True,
                        "message": "User Registration Successfull, Please check your email and verify using OTP",
                        "status": status.HTTP_201_CREATED,
                        'user_id': user.id,
                        "user_name": user.name,
                        "user_phone": str(user.phone),
                        "user_email": user.email,
                    }
                    return Response(response, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({
                    "message":str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response({
                "message": "Data not found"
            }, status=status.HTTP_400_BAD_REQUEST)
                
                
class UserLoginWithEmail(APIView):
    
    def get(self, request, *ags, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = User.objects.filter(email=email)
            if user:
                email = User.objects.get(email=email)
                user_validate = authenticate( username=email, password=password)
                if user_validate:
                           response={
                                "success": True,
                                "message": "User logged in Successfully",
                                "status": status.HTTP_201_CREATED,
                                'user_id': user._id,
                                "user_name": user_validate.name,
                                "user_phone": str(user_validate.phone),
                                "user_email": user_validate.email,
                            }
                           return Response(response, status=status.HTTP_201_CREATED)
            # return Response( status=status.HTTP_400_BAD_REQUEST)
                return Response({
                        'message': "username or password does not match!! please enter correct credentials"
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                        'message': "User Dose Not Exist"
                },status=status.HTTP_400_BAD_REQUEST)
                

                    