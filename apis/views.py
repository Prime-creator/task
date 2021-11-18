from types import MappingProxyType
from django.shortcuts import render
from .models import Meds
from .serializers import MedsSerializer
from rest_framework.views import APIView
from rest_framework.response import *
from rest_framework import status
# Create your views here.


class FetchMeds(APIView):
    def get(self,request):
        medicineName = request.data.get("medicineName")
        obj = Meds.objects.filter(sku_name=medicineName)
        if(len(obj)==0):
            return Response({"message":"no data found","data":None},status=status.HTTP_404_NOT_FOUND)
        resp = list()
        data = MedsSerializer(obj,many=True)
        return Response({"message":"data found","data":data.data},status=status.HTTP_200_OK)