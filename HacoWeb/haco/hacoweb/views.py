from django.shortcuts import render
import requests


def weather(request):
    url = "http://api.openweathermap.org/data/2.5/weather?lat=55.0&lon=6.02&appid=518b54b7cfd7c1047999fb4815eab4a5"

    if request.method == "POST":
        pass

    weather_data = []


def home(response):
    return render(response, 'hacoweb/index.html')


def glossary(response):
    return render(response, 'hacoweb/glossary.html')
