from django.db.models import query
from django.shortcuts import render, redirect, reverse
from .models import Ticket
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TicketModelForm,TicketCreateForm
from django.urls import reverse_lazy



class TicketListView(ListView):
    template_name = 'ticket_list.html'
    queryset = Ticket.objects.all()
    context_object_name = 'tickets'




class TicketCreateView(CreateView):
    template_name = 'ticket_create.html'
    form_class = TicketCreateForm
    
    def get_success_url(self):
        print("self.request.GET:", self.request.GET.get("from"))
        coming_from = self.request.GET.get("from")
        url_name = 'tickets:ticket-list'
        if coming_from == "home":
            url_name = "website:landind_page"
        return reverse(url_name)

    def form_valid(self, form):
        print("in form_valid")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("in form_invalid")
        return super().form_invalid(form)


class TicketDetailView(DetailView):
    template_name = 'ticket_detail.html'
    queryset = Ticket.objects.all()
    context_object_name = 'ticket'



class TicketUpdateView(UpdateView):
    template_name = 'ticket_update.html'
    form_class = TicketModelForm
    queryset = Ticket.objects.all()

    
    def get_success_url(self):
        obj = self.get_object()
        return reverse_lazy('tickets:ticket-detail', kwargs={'pk': obj.pk})



class TicketDeleteView(DeleteView):
    template_name = 'ticket_delete.html'
    queryset = Ticket.objects.all()

    def get_success_url(self):
        return reverse('tickets:ticket-list')