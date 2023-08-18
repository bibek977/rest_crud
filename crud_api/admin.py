from django.contrib import admin
from .models import *

@admin.register(Film)
class FilmModel(admin.ModelAdmin):
    list_display = ['id', 'Title', 'Year', 'Director' , 'imdbRating']