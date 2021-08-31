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


# Send data to the report for storing in the database
def sendreport(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            if 'reportIncident' in response.POST:
                report_incident = response.POST['reportIncident']


# Report view
def report(response):
    # Grab the user from the response
    user = response.user

    return render(response, 'hacoweb/report_tool.html')

    # Check if it's authenticated

    # if user.is_authenticated:
    #     return render(response, 'hacoweb/report_tool.html')  # let them through if authenticated
    # else:
    #     base_url = reverse('login')  # else build a response header and post it in the redirect
    #     query = urlencode({'auth': 'noauth'})
    #     url = '{}?{}'.format(base_url, query)
    #     return redirect(url, permanent=False)


def glossary(response):
    return render(response, 'hacoweb/glossary.html')
