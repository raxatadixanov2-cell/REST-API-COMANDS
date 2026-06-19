from django.contrib import admin
from .models import ApexModel


class ApexModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


admin.site.register(ApexModel, ApexModelAdmin)
