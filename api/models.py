from django.db import models


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    founded = models.IntegerField()

    def __str__(self):
        return str(self.name)
