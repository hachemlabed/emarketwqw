from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("You have provided a valid email")
        user = self.model(email=self.normalize_email(email), **extra_fields)  
        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email,password=password )
        user.is_superuser= True
        user.is_staff= True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(blank=False, default='', unique=True)
    username = models.CharField(blank=False, default='', unique=True, max_length=20)
    password = models.CharField( max_length=128, blank=False, default='' )
    confirm_password = models.CharField( max_length=128, blank=False, default='')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username' 
    EMAIL_FIELD = 'email'
    objects = UserManager()


    