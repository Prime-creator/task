from types import MappingProxyType
from django.shortcuts import render
from .models import Meds
from .serializers import MedsSerializer
from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import status
# Create your views here.

#this code is optimised with the use of concept of indexing in mysql.
class FetchMeds(APIView):
    def get(self,request):
        medicineName = request.data.get("medicineName")
        medsArray = medicineName.split(" ")
        resp = {}
        
        for med in medsArray:
            obj = Meds.objects.filter(sku_name__contains=med)
            if(len(obj)==0):
                pass
            else:
                print("else")
                for data in list(obj.iterator()):
                    d={
                        "sku_id":data.sku_id, 
                        "product_id":data.product_id, 
                        "sku_name":data.sku_name, 
                        "price":data.price,
                        "manufacturer_name":data.manufacturer_name, 
                        "salt_name":data.salt_name, 
                        "drug_form":data.drug_form, 
                        "Pack_size":data.Pack_size, 
                        "strength":data.strength, 
                        "product_banned_flag":data.product_banned_flag, 
                        "unit":data.unit, 
                        "price_per_unit":data.price_per_unit
                    }
                    resp[d["sku_id"]]=d
                
        return Response({"message":"data found","data":resp.values()},status=status.HTTP_200_OK)