from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product
from django.http import JsonResponse
from rest_framework import generics,viewsets
from .serializers import ProductSerializer

class ProductView(viewsets.ModelViewSet):
   
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def get():
        products = list(Product.objects.values())
        return JsonResponse(products, safe=False)

    

