from django.contrib import admin
from .models import EchoModel


class EchoModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


admin.site.register(EchoModel, EchoModelAdmin)
