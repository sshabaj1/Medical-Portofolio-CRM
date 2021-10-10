from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from tickets.forms import TicketCreateForm

class LandindPageView(TemplateView):
    template_name = 'index.html'
    form_class = TicketCreateForm

    def get_success_url(self):
        return reverse('landind_page')
