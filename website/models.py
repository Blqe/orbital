# Create your models here.

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    efficieny_of_police = models.IntegerField(max_value=5, min_value=0)
    how_safe_you_feel = models.IntegerField(max_value=5, min_value=0)
    helpfulness_of_locals = models.IntegerField(max_value=5, min_value=0)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.IntegerField()
    lng = models.IntegerField()
    postal_code = models.IntegerField()

#class User(models.Model):
#    name = models.CharField(max_length=50)
#    email = models.CharField(max_length=50)
