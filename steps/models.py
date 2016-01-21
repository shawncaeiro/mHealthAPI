from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Health(models.Model):
    date_taken = models.DateField(auto_now_add = True)
    step_count = models.IntegerField()