from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.views import LoginView   
from django.contrib.auth import logout
from django.contrib.messages import constants as messages
from django.urls import reverse_lazy
from .forms import UserCreateForm


class DashboardView(TemplateView):
    template_name = 'dashboard.html'




class UserLoginView(LoginView):
    template_name = 'login.html'


def logout_request(request):
    logout(request)
    return redirect("users:login")


class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('users:dashboard')
    







