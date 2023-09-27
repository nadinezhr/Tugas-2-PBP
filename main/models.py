from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.IntegerField()
    picture = models.URLField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
