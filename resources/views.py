from django.views.generic import ListView
import requests
import config
from .models import CurrentGear, writecurrentgear


def netboxdata():
    """
    Goes to poll the data and serve/write to DB. If it can't get it, it will grab the database
    """
    current = False
    dcim = "devices"
    apiUrl = "https://netbox.squirrelco.net/api/dcim/"
    try:
        auth_header = {'Authorization': f'Token {config.NETBOXAPI}'}
        response = requests.get(apiUrl + f"{dcim}", headers=auth_header)
        if response.status_code == 200:
            data = response.json()
            current = True
            CurrentGear.objects.all().delete()
            for entry in data["results"]:
                if entry["device_type"]["manufacturer"]["name"] != "Generic":
                    if entry["tenant"]["name"] == "HSBXL":
                        if entry["status"]["value"] == "active":
                            writecurrentgear(entry)
    except:
        print("server was unreachable")
    return current


class Devicelist(ListView):
    model = CurrentGear
    template_name = 'resources.html'
    context_object_name = 'devices'

    def get_queryset(self):
        # Order the queryset by the 'name' field in ascending order (alphabetical)
        return CurrentGear.objects.all().order_by('room')

    def get_context_data(self, **kwargs):
        # First executes the netbox function. Because if it fails with another code than 200, it will return false
        netbox = netboxdata()
        context = super().get_context_data(**kwargs)
        context["wasExecuted"] = netbox
        return context
