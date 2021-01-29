from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.
# Personalised register view
def register(response):
    form = RegistrationForm()
    return render(response, 'users/register.html', {form: "form"})
