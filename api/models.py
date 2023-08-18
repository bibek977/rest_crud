from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    imdb = models.FloatField()
    director= models.CharField(max_length=50)
    runtime= models.IntegerField()

    def __str__(self):
        return self.title