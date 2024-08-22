from rest_framework import serializers

from .models import Product,SKU,ProductImage

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = {'category','url','title','price','MRP','last_7_day_sale'\
                   ,'fit','fabric','neck','sleeve','pattern','length'\
                    ,'description'}

class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = {'product','color','size'}  # fields

class ProductImage(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = {'product','image_url'}  # fields