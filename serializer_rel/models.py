from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    duration = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.title

# class Album(models.Model):
#     cover = models.CharField(max_length=100)
#     song = models.ForeignKey(Song, on_delete=models.CASCADE,related_name='album')
#     year = models.IntegerField()