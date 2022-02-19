from django.db import models
from User.models import New


# Create your models here.
class Event(models.Model):
    creator = models.ForeignKey(
        New, related_name='create', on_delete=models.CASCADE)
    csv_file = models.FileField(upload_to='/media/documents/')
    question = models.ForeignKey(Question)


class Question(models.Model):
