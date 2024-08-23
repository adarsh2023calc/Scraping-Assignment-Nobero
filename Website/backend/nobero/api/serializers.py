from rest_framework import serializers

from .models import Product,SKU,ProductImage

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__' # fields

class ProductImage(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__ '# fields