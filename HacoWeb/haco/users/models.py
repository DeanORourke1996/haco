from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Overide auth_user model with custom properties
# User management class
class UserManagement(BaseUserManager):

    def create_user(self, email, username, password, first_name=None, last_name=None):
        if not email:
            raise ValueError("Email address is required")
        if not username:
            raise ValueError("Username is required")

        # Fill the model with parameter data
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name=None, last_name=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


# Define a user
class User(AbstractBaseUser):
    # Custom model elements
    username = models.CharField('Username', primary_key=True, max_length=150)
    password = models.CharField('User Password', null=False, max_length=150)
    first_name = models.CharField('First Name', null=True, max_length=50)
    last_name = models.CharField('Last Name', null=True, max_length=50)
    country = models.CharField('Country', null=True, max_length=56)  # longest country name in the world is 56 chars

    # Required for method overide
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)
    last_login = models.DateTimeField('Last Login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField('Email Address', null=False, max_length=150, unique=True)

    # Type objects
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManagement()

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @staticmethod
    def has_module_perms(app_label):
        return True


