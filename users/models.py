from django.db import models



class User(models.Model):
    username = models.CharField(max_length=255)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    password = models.CharField(max_length=250, default='Tirane2021.')

    def __str__(self):
        return self.username

