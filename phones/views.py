from django.views.generic import TemplateView


class Phone(TemplateView):
    template_name = 'phones.html'
