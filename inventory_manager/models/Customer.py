from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    address = models.CharField(max_length=256)