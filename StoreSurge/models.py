from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Period(models.Model):
    registers_open = models.IntegerField(default=0)
    wifi_devices = models.IntegerField(default=0)
    time_field = models.DateTimeField('Time')
