from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Overide auth_user model with custom properties
# User management class
class UserManagement(BaseUserManager):

    def create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError("Email address is required")
        if not username:
            raise ValueError("Username is required")
        if not password:
            raise ValueError("Password is required")

        # Fill the model with parameter data
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            **kwargs
        )

        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, email, username, password, **kwargs):
        # Set defaults for staffuser account
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Staff must be assigned Staff permissions')
        if kwargs.get('is_active') is not True:
            raise ValueError('Creating a new user must immediately make that user active.')
        if kwargs.get('is_superuser') is not False:
            raise ValueError('There must only be one superuser within this system')

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            **kwargs
        )

        user.save(using=self._db)
        return self.create_user(email, username, password, **kwargs)


# Define a user
class User(AbstractBaseUser, PermissionsMixin):
    # Custom model elements
    username = models.CharField('Username', primary_key=True, max_length=150)
    password = models.CharField('User Password', null=False, max_length=150)
    first_name = models.CharField('First Name', null=True, max_length=50)
    last_name = models.CharField('Last Name', null=True, max_length=50)
    country = models.CharField('Country', blank=True, null=True, max_length=56)  # longest country name is 56 chars

    # Required for method overide
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True, null=True)
    last_login = models.DateTimeField('Last Login', auto_now_add=True, null=True)
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


