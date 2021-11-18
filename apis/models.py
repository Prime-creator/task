from django.db import models
from datetime import datetime
# Create your models here.

class Meds(models.Model):
    sku_id=models.IntegerField(null=True)
    product_id=models.IntegerField(null=True)
    sku_name=models.CharField(null=True,max_length=100)
    price=models.FloatField(null=True)
    manufacturer_name=models.CharField(null=True,max_length=100)
    salt_name=models.CharField(null=True,max_length=100)
    drug_form=models.CharField(null=True,max_length=100)
    Pack_size=models.CharField(null=True,max_length=100)
    strength=models.CharField(null=True,max_length=100)
    product_banned_flag=models.BooleanField(null=True)
    unit=models.CharField(null=True,max_length=100)
    price_per_unit=models.IntegerField(null=True)