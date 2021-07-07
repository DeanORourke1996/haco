from events.data_funcs import modis_record_fetch, write_modis_data
from django.views.generic import DetailView
from events.models import Event


class EventDetail(DetailView):
    template_name = 'events/event-inspect.html'
    model = Event


def parse_events(request):

    if request.method == "GET":
        # Get events from server
        events = Event.objects.filter()