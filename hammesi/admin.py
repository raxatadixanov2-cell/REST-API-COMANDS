from django.contrib import admin

# Register your models here.
from .models import HammesiModel

class HammesiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age')


admin.site.register(HammesiModel, HammesiAdmin)