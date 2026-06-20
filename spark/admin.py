from django.contrib import admin
from .models import SparkModel


class SparkModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


admin.site.register(SparkModel, SparkModelAdmin)
