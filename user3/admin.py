# admin.py
from django.contrib import admin
from .models import timeModel


class timeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "age")


admin.site.register(timeModel, timeModelAdmin)