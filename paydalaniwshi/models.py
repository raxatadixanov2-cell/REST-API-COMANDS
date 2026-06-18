from django.db import models

# Create your models here.
class PaydalaniwshiModel(models.Model):
    ati = models.CharField(max_length=100)
    fm = models.CharField(max_length=100)


    def __str__(self):
        return self.ati