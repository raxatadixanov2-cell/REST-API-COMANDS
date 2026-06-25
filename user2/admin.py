from django.contrib import admin
from .models import apsModel

# Register your models here.

class apsModelAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'surname', 'age')
    
admin.site.register(apsModel, apsModelAdmin)    
