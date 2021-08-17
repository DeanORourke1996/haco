from django.shortcuts import render
from django.db.models import Q
from events.models import Event
import datetime


def home(response):
    from json import dumps
    # Set expiry on session
    response.session.set_expiry(300)

    # Collects days events when gathered
    latest_events = Event.objects.filter(
        Q(confidence__contains='high') |
        Q(confidence__contains='nominal'),
        acq_date__contains=str(datetime.date.today())
    )
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
