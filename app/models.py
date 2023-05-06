from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    
    
    def create_user(self, email, phone, password=None, **extra_fields):
        
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email = email, password=password, phone=phone)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    
    def create_superuser(self, email, phone = None, password=None, **extra_fields):
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_superuser', True)
       extra_fields.setdefault('is_active', True)

       if extra_fields.get('is_staff') is not True:
        raise ValueError(('Superuser must have is_staff=True.'))
        
            
       return self.create_user(self, email, phone = None, password=None, **extra_fields)

        
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    password = models.CharField(max_length=8)
    forgot_password = models.CharField(max_length=8, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    last_logout = models.DateTimeField(null=True, blank=True)
    
    objects = UserManager()
    REQUIRED_FIELDS = []
    
    USERNAME_FIELD = 'email'