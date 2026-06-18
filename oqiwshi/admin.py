from django.contrib import admin

# Register your models here.
from .models import OqiwshiModel


class OqiwshiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'age')


admin.site.register(OqiwshiModel, OqiwshiAdmin)