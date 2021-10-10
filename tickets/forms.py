from django import forms
from .models import Ticket


class TicketModelForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'cl_name',
            'cl_phone',
            'cl_email',
        )


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'cl_name',
            'cl_phone',
            'cl_email',
            'ticket_subject', 
            'cl_message'
        )

