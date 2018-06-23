from __future__ import unicode_literals
from django.db import models

class Testline(models.Model):
    project = models.GenericIPAddressField()
    dltput = models.CharField(max_length=200,default="N/A")
    rsrp = models.CharField(max_length=200,default="N/A")
    sinr = models.CharField(max_length=200,default="N/A")
    cell = models.CharField(max_length=200,default="N/A")
    mode = models.CharField(max_length=200,default="N/A")
    tput_range = models.CharField(max_length=200,default="N/A")
    def __unicode__(self):
        return self.project


