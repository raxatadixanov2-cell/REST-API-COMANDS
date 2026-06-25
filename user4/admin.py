from django.contrib import admin
from .models import canModel

# Register your models here.

class canModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "age") 

admin.site.register(canModel, canModelAdmin)        

