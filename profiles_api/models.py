from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManger(BaseUserManager):
    """Mnager for user profiles"""

    def create_user(self, email, name, passowrd=None):
        """Create a niew user profile"""
        if not email:
            raise ValueError('User must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(passowrd)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save superuser"""
        user = self._create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """Retrive full nave of user """
        return self.name

    def get_short_name(self):
        """Retrive short nave of user """
        return self.name

    def __str__(self):
        """Return string represntatiton of user"""
        return self.email

