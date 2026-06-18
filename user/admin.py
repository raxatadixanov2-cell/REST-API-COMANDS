from django.contrib import admin

# Register your models here.
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')


admin.site.register(UserModel, UserAdmin)
