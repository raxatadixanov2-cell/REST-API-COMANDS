from django.contrib import admin
from .models import FluxModel


class FluxModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


admin.site.register(FluxModel, FluxModelAdmin)
