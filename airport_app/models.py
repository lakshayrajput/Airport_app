# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import uuid

# Create your models here.
class CustomerModel(models.Model):
    mob_no = models.IntegerField(default=10)
    aadhaar_no = models.IntegerField(default=12)
    otp_no = models.IntegerField(default=8)
