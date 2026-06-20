from django.db import models

# Create your models here.
class dataModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self):
        return self.surname