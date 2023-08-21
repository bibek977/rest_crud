from django.db import models

# Create your models here.
class Intern(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    location = models.CharField(max_length=50)
    program = models.CharField(max_length=50)

    def __str__(self):
        return self.name