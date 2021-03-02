from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass



class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    label = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, blank=True)
    release_date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="albums")
    #artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name="artists")
    #artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title



