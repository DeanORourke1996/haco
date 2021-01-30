from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages


# Create your views here.
# Personalised register view
def register(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            messages.success(response, f'Account created for {username}')
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(response, 'users/register.html', {'form': form})
