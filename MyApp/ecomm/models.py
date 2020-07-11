# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProductInformation(models.Model):
    CATEGORY_CHOICES = (
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Cosmetics', 'Cosmetics'),
        ('Stationary', 'Stationary'),
        ('Sports', 'Sports'),
    )
    name = models.CharField(max_length = 32)
    price = models.FloatField()
    category = models.CharField(max_length = 32, choices = CATEGORY_CHOICES)
    company = models.CharField(max_length = 32)
    quantity = models.IntegerField()
    description = models.TextField(blank = True)
    