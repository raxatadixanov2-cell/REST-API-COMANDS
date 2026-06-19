from django.contrib import admin
from .models import NovaModel


class NovaModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


admin.site.register(NovaModel, NovaModelAdmin)
