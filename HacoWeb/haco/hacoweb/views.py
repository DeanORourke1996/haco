from django.shortcuts import render
from events.models import Event
import datetime


def weather(request):
    url = "http://api.openweathermap.org/data/2.5/weather?lat=55.0&lon=6.02&appid=518b54b7cfd7c1047999fb4815eab4a5"

    if request.method == "POST":
        pass

    weather_data = []


def home(response):
    from json import dumps
    # Collects days events when gathered
    latest_events = Event.objects.filter(acq_date=datetime.date.today())
    # Create a list
    event_list = [le.serialize() for le in latest_events]
    # Dictionary
    event_dict = {
        "type": "FeatureCollection",
        "features": event_list
    }
    # Serialize
    event_json = dumps(event_dict)
    # Context variable
    context = {'latest_events': event_json}

    return render(response, 'hacoweb/index.html', context)


def glossary(response):
    return render(response, 'hacoweb/glossary.html')
