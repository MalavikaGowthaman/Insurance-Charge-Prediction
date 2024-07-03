from django.db import models

# Create your models here.
class ckdModel(models.Model):



    age = models.FloatField()
    # Age=models.IntegerField()
    sex = models.FloatField()
    bmi  =models.FloatField()
    children = models.FloatField()
    smoker = models.FloatField()
