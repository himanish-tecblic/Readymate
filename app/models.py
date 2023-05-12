from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email = email,password=password, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        print(user.password)
        return user
    
    
    def create_superuser(self, email, password, **extra_fields):
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_superuser', True)
       extra_fields.setdefault('is_active', True)

       if extra_fields.get('is_staff') is not True:
        raise ValueError(('Superuser must have is_staff=True.'))
        
            
       return self.create_user(email, password, **extra_fields)
   
    def create(self, **kwargs):
        return self.model.objects.create_user(**kwargs)
    
    


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    password = models.CharField(max_length=8)
    forgot_password = models.CharField(max_length=8, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    last_logout = models.DateTimeField(null=True, blank=True)
    
    objects = UserManager()
    REQUIRED_FIELDS = []
    
    USERNAME_FIELD = 'email'

    def save(self,*args,**kwargs):
        self.password = make_password(self.password)
        super(User,self).save(*args,**kwargs)