from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100, blank=False)
    auth_token = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=20, blank=False)
    contact = models.CharField(max_length=12, blank=False)
    whatsapp = models.CharField(max_length=12, blank=False)
    age = models.CharField(max_length=12, blank=False)
    city = models.CharField(max_length=20, blank=False)
    date= models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Birthday(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to="Birthday", blank=False)

    def __str__(self):
        return self.name
