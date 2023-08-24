from django.db import models

class Film(models.Model):
    Title = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Director = models.CharField(max_length=100)
    Writer = models.CharField(max_length=100)
    Actors = models.CharField(max_length=100)
    Actress = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Year = models.IntegerField()
    imdbRating = models.IntegerField()
    Runtime = models.IntegerField()

    def __str__(self):
        return self.Title
