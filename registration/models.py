from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=256)
    message = models.TextField()
    ctime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





class UserDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=100)

    # Add more fields as needed

    def __str__(self):
        return self.email
