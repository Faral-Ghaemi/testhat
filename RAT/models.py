from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Credit(models.Model):
    number = models.IntegerField(default=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
