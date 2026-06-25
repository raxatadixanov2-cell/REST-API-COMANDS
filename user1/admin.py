from django.contrib import admin
from .models import dataModel

# Register your models here.

class dataModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age')

admin.site.register(dataModel, dataModelAdmin)      
