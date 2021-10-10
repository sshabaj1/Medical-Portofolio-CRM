from django.db import models


class Ticket(models.Model):
    cl_name = models.CharField(max_length=255)
    cl_phone = models.CharField(max_length=255)
    cl_email = models.CharField(max_length=255)
    ticket_subject = models.CharField(max_length=255)
    cl_message = models.CharField(max_length=250)


    def __str__(self):
        return f'{self.cl_name} {self.cl_phone}'
