from django.contrib.auth.forms import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User


# Register for Haco
class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Enter a Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Re-Enter Password', widget=forms.PasswordInput())
    first_name = forms.CharField(label='First Name', required=False)
    last_name = forms.CharField(label='Last Name', required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]


# Login with Haco
class LoginForm(UserCreationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "password"]
