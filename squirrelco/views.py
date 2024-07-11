from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class Peering(TemplateView):
    template_name = 'peering.html'


class Sponsors(TemplateView):
    template_name = 'sponsors.html'


class Oid(TemplateView):
    template_name = 'oid.html'


class Squirrel(TemplateView):
    template_name = 'squirrel.html'


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
