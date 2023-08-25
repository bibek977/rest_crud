from django.contrib import admin
from .models import *

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'country',
        'gender',
        'age'
    ]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = [ 'title' , 'singer' , 'year']