from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Foods
from .serializers import FoodSerializers

class SearchProduct(APIView):
    def get(self,request,format=None):
        pfilter = {}
        if request.GET.get('product_name'):
            pfilter['product'] = request.GET.get('product_name')
        return self.res(**pfilter)

    def post(self,request,format=None):
        pfilter = {}
        if request.data.get('product_name'):
            pfilter['product'] = request.data.get('product_name')
        return self.res(**pfilter)

    def res(self,**pfilter):
        return_data = {}
        product = Foods.objects.filter(**pfilter)
        fs = FoodSerializers(product,many=True)
        fdata = fs.data
        return_data['status'] = 'success'
        return_data['results'] = [
            fdata
        ]
        return Response(return_data)


