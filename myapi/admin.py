from django.contrib import admin
from .models import Hero, Peple



admin.register(Hero,Peple)(admin.ModelAdmin)
