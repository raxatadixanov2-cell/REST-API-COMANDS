from django.db import models

# Create your models here.
class OqiwshiModel(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self):
        return self.username