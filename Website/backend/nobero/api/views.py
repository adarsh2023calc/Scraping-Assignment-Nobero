from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product
from django.http import JsonResponse
from rest_framework import generics
from .serializers import ProductSerializer

class ProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
    

