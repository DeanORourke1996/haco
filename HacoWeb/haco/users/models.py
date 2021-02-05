from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManagement(BaseUserManager):

    def create_user(self, email, username, password):
        if not email:
            raise ValueError("Email address is required")
        if not username:
            raise ValueError("Username is required")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class User(AbstractBaseUser):
    username = models.CharField('Username', primary_key=True, max_length=150)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)
    last_login = models.DateTimeField('Last Login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField('Email Address', null=False, max_length=150, unique=True)
    password = models.CharField('User Password', null=False, max_length=150)
    first_name = models.CharField('First Name', null=True, max_length=50),
    second_name = models.CharField('Last Name', null=True, max_length=50),
    country = models.CharField('Country', null=True, max_length=56)  # longest country name in the world is 56 chars

    # Type objects
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    objects = UserManagement()

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @staticmethod
    def has_module_perms(app_label):
        return True


