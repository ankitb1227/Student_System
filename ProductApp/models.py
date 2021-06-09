from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()
    # USERNAME_FIELD = 'name'
    def __str__(self):
        return self.name