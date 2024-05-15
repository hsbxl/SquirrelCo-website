from django.contrib import admin
from .models import Giveawaygear


class gear(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "software", "lastEdition")


admin.site.register(Giveawaygear, gear)
