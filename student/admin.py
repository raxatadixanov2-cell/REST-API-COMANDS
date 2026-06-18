from django.contrib import admin

# Register your models here.
from .models import StudentModel

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')



admin.site.register(StudentModel, StudentAdmin)