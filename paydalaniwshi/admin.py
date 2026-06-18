from django.contrib import admin

# Register your models here.
from .models import PaydalaniwshiModel


class PaydalaniwshiAdmin(admin.ModelAdmin):
    list_display = ('id', 'ati', 'fm')


admin.site.register(PaydalaniwshiModel, PaydalaniwshiAdmin)