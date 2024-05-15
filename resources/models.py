from django.db import models


class CurrentGear(models.Model):
    """
    Will contain a copy of the latest fetched data from Netbox
    """
    netboxid = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=60)
    room = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    software = models.CharField(max_length=60)
    lastEdition = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.netboxid

    class Meta:
        indexes = [
            models.Index(fields=["manufacturer"]),
            models.Index(fields=["model"]),
        ]


def writecurrentgear(entry):
    db = CurrentGear()
    db.id = entry["id"]
    db.manufacturer = entry["device_type"]["manufacturer"]["name"]
    db.model = entry["device_type"]["model"]
    db.room = entry["location"]["name"]
    db.role = entry["role"]["name"]
    db.software = entry["platform"]["name"]
    db.save()
