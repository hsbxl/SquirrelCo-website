from django.http import HttpResponse
from django.views.generic import ListView
import requests
import config
from .models import Giveawaygear, writegiveaway


def netboxdata():
    """
    Goes to poll the data and serve/write to DB. If it can't get it, it will grab the database
    """
    current = False
    dcim = "devices"
    apiUrl = "https://netbox.squirrelco.net/api/dcim/"
    auth_header = {'Authorization': f'Token {config.NETBOXAPI}'}
    try:
        response = requests.get(apiUrl + f"{dcim}", headers=auth_header)
        if response.status_code == 200:
            data = response.json()
            current = True
            Giveawaygear.objects.all().delete()
            for entry in data["results"]:
                if entry["device_type"]["manufacturer"]["name"] != "Generic":
                    if entry["tenant"]["name"] == "HSBXL":
                        if entry["comments"] == "donnation":
                            writegiveaway(entry)
    except:
        print("Server unreachable")
    return current


class GiveawayList(ListView):
    model = Giveawaygear
    template_name = 'giveaway.html'
    context_object_name = 'devices'

    def get_queryset(self):
        # Order the queryset by the 'name' field in ascending order (alphabetical)
        return Giveawaygear.objects.all().order_by('model')

    def get_context_data(self, **kwargs):
        # First executes the netbox function. Because if it fails with another code than 200, it will return false
        netbox = netboxdata()
        context = super().get_context_data(**kwargs)
        context["wasExecuted"] = netbox
        return context
