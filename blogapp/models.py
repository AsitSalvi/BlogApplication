from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 


#------------------User Model---------------------------
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        phone = extra_fields.get('phone')
        if not email:
            raise ValueError('Users must have an email address')
        if not phone:
            raise ValueError('Users must have an phone number')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.phone = phone
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['phone', ]
    USERNAME_FIELD = 'email'

    objects = UserManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

      
      
#-----------------------Blog Model------------------------------
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
