from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'program']