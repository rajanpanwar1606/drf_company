from django.db import models

# Create your models here.
from django.db import models


TYPES_CHOICES = [
    ('IT', 'IT'),
    ('NON IT', 'Non IT'),
    ('mobile phones', 'Mobile Phones'),
]
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length=50,null=True,blank=True)
    about = models.TextField(null=True,blank=True)
    types = models.CharField(max_length=100, choices=TYPES_CHOICES,null=True,blank=True)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    