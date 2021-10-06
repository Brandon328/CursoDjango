# Django
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH


class User(models.Model):
    # django ya agrega un id por defecto
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField()
    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    country = models.CharField(max_length=25, null=True)
    city = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.first_name + " : " + self.city + " : " + self.country
