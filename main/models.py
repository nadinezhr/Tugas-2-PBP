from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.IntegerField()
    picture = models.URLField(max_length=100)
