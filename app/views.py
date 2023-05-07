from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
import requests

# Create your views here.



class UserRegistration(APIView):

    def post(self, request, *args, **kwargs):
        print("----------------------------------")
        if request.data:
            data = request.data
            # print("------------------------->>>>",data)
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