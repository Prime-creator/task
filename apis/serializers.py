from django.db.models import fields
from rest_framework import serializers
from .models import Meds

class MedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meds
        fields = ("sku_id", "product_id", "sku_name", "price",
                  "manufacturer_name", "salt_name", "drug_form", "Pack_size", "strength", "product_banned_flag", "unit", "price_per_unit")
