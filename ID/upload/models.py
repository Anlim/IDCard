# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IMG(models.Model):
    img = models.ImageField(upload_to='material') #图片存储位置
