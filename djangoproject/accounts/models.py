from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        now = datetime.now()
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, **extra_fields)
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, username, email, password, **extra_fields):
        u = self.create_user(username, email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=100, unique=True)
    email = models.EmailField('email address', max_length=255, unique=True)
    mobile = models.CharField('mobile number', max_length=30)
    
    created_at = models.DateTimeField('created date', auto_now_add=True, blank=True, null=True)
    
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin '
                    'site.')
    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
                    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'mobile']
    
    def __unicode__(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
