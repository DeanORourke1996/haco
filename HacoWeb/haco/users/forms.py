from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput


class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
