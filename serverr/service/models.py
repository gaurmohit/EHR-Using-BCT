from django.db import models
import threading

# Create your models here.
class ThreadManage(models.Model):
    task = models.CharField(max_length = 20, blank=True, null=True)
    status = models.BooleanField(default=False, blank=False)