from django.shortcuts import render
from django.views.generic import TemplateView

class LandindPageView(TemplateView):
    template_name = 'index.html'
