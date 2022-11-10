from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.http import Http404
from django.conf import settings

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
        product = Foods.objects.filter(**pfilter).order_by('-id')
        # Pagination
        try:
            if 'page' in self.request.query_params:
                page_number = self.request.query_params.get('page', 1)
                product = Paginator(product , settings.PAGINATION_COUNT).page(page_number)
        except EmptyPage:
            raise Http404()

        fs = FoodSerializers(product,many=True)
        return_data['status'] = 'success'
        return_data['results'] = [
            fs.data
        ]
        return Response(return_data)


