from django.http import HttpResponse
from django.db import DatabaseError
from django.contrib import messages
import json
from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from events.models import Event
import datetime


def home(response):
    # Set expiry on session
    response.session.set_expiry(300)

    # Collects days events when gathered
    latest_events = Event.objects.filter(
        Q(confidence__contains='high') |
        Q(confidence__contains='nominal') |
        Q(confidence__contains='moderate') |
        Q(confidence__contains='severe'),
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
    event_json = json.dumps(event_dict)
    # Context variable
    context = {'latest_events': event_json}

    return render(response, 'hacoweb/index.html', context)


# Send data to the report for storing in the database
def sendreport(response):
    # Instantiate variables each call
    lat = lng = severity = None

    # Check method
    if response.method == "POST":
        # Check initial values being returned
        if 'latitude' and 'longitude' and 'severity' and 'user_reported' in response.POST:
            # Grab values from POST
            lat = response.POST['latitude']
            lng = response.POST['longitude']
            severity = response.POST['severity']

            try:
                # Begin Database Pre-processing
                e = Event.objects.get_or_create(
                    lat=lat,  # latitude
                    lon=lng,  # longitude
                    confidence=severity,  # severity
                    acq_date=datetime.date.today(),  # today datetime
                    acq_time=datetime.datetime.now().time(),
                    is_user_made='T'  # Is a user created entry
                )
                messages.success(response, "Incident was recorded. Thank you for your contribution")
                r = {'status': 1, 'message': 'success'}
                return HttpResponse(json.dumps(r), content_type='application/json')
            except DatabaseError as dbe:
                r = {'status': 0, 'message': 'failed on database'}
                print("Error with database insertion: " + str(dbe))
                return HttpResponse(json.dumps(r), content_type='application/json')

        else:
            r = {'status': 0, 'message': 'failed on value errors'}
            return HttpResponse(json.dumps(r), content_type='application/json')
    else:
        r = {'status': 0, 'message': 'Inavlid request method'}
        return HttpResponse(json.dumps(r), content_type='application/json')


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
