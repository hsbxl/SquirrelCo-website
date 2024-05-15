"""
URL configuration for squirrelco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from .views import Index, Peering, Sponsors, Squirrel
from resources.views import Devicelist
from giveaway.views import GiveawayList
from phones.views import Phone
from django.views.generic.base import RedirectView, TemplateView

favicon_view = RedirectView.as_view(url='https://static.squirrelco.net/images/squirrel-white.png', permanent=True)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("peering.html", Peering.as_view(), name="peering"),
    path("sponsors.html", Sponsors.as_view(), name="sponsors"),
    path("squirrel.html", Squirrel.as_view(), name="squirrel"),
    path("resources.html", Devicelist.as_view(), name="resources"),
    path("giveaway.html", GiveawayList.as_view(), name="giveaway"),
    path("phone.html", Phone.as_view(), name="phone"),
    re_path(r'^favicon\.ico$', favicon_view),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('admin/', admin.site.urls),
]
