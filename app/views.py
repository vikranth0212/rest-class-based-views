from django.shortcuts import render
from app.serializers import *
from app.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class product_view(APIView):
    def get(self,request):
        POD=product.objects.all()
        JOD=productserializer(POD,many=True)
        return Response(JOD.data)

    def post(self,request):
            JDO=request.data
            PDO=productserializer(data=JDO)
            if PDO.is_valid():
                PDO.save()
                return Response({'insert':'Data is inserted successfully'})
            else:
                return Response({'not':'inserted data is not valid'})
    

