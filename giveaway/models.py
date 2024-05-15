from django.db import models


class Giveawaygear(models.Model):
    """
    Will contain a copy of the latest fetched data from Netbox
    """
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=60)
    software = models.CharField(max_length=60)
    lastEdition = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.manufacturer

    class Meta:
        indexes = [
            models.Index(fields=["manufacturer"]),
            models.Index(fields=["model"]),
        ]


def writegiveaway(entry):
    db = Giveawaygear()
    db.manufacturer = entry["device_type"]["manufacturer"]["name"]
    db.model = entry["device_type"]["model"]
    db.software = entry["platform"]["name"]
    db.save()
