from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bakery(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.quantity)
