from decouple import config
from twilio.rest import Client
import random
from .models import User
import os

def send_otp_via_phone(phone):
    account_sid = 'AC06ff74ca3c87d76dd036274038d61c74'
    auth_token = '3b6614a5f04d42e1e6479d97343bedf1'
    client = Client(account_sid, auth_token)
    user = User.objects.get(phone=phone)
    if user:
        phone_number = phone
        my_otp = random.randint(1111, 9999)
        message = client.messages.create(
            body=f"Hi ,Welcome, this is your otp {my_otp}",
            from_='+16406008939',
            to=f'{phone_number}'
        )
        User.objects.filter(phone=phone).update(otp=my_otp)