from django.shortcuts import render, redirect
from users.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Register view
def user_register(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            # Can be saved once valid
            form.save()
            # Clean inputs
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(response, f'Account created for {username}')
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(response, 'users/register.html', {'form': form})


# Login view
def user_login(response):
    pass


# Logout view
def user_logout(response):
    logout(response)
    return redirect('home')
