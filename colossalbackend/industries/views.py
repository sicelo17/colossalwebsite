from django.db.models import Q 
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view 

from .models import Category, Industry
from .serializers import CategorySerializer, IndustrySerializer


class ProductList(APIView):
    def get(self, request, format=None):
        products = Industry.objects.all()
        serializer = IndustrySerializer(products, many=True)
        return Response(serializer.data)

    
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Industry.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Industry.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = IndustrySerializer(industry)     #getting data from serializers.py
        return Response(serializer.data)
