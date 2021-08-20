from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)
    message = models.CharField(max_length=200)

    def __str__(self) :
        return self.name