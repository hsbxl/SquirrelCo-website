from django.contrib import admin
from .models import CurrentGear


class gear(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "room", "software", "lastEdition")


admin.site.register(CurrentGear, gear)
