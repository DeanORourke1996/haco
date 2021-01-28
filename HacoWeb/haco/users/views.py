from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
# Personalised login view
def login(request):
    return render(request, 'users/login.html')
