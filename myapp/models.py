from django.db import models

class Product(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

