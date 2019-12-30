from django.db import models
from datetime import datetime, timedelta


# Create your models here.


class store(models.Model):
    key = models.CharField(max_length=100)
    value =models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.now)



