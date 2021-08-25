from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
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


# Report view
def report(response):
    # Grab the user from the response
    user = response.user
    # Check if it's authenticated
    if user.is_authenticated:
        return render(response, 'hacoweb/report_tool.html')  # let them through if authenticated
    else:
        base_url = reverse('register')  # else build a response header and post it in the redirect
        query = urlencode({'auth': 'noauth'})
        url = '{}?{}'.format(base_url, query)
        return redirect(url, permanent=False)


def glossary(response):
    return render(response, 'hacoweb/glossary.html')
