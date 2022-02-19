from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class New(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    creator = models.BooleanField(default=False)
