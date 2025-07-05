from rest_framework import serializers
from .models import Products, Category, CustomUser

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'slug', 'image', 'price']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name','description', 'slug', 'image', 'price']

class CategoryListSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name',  'image', 'slug']

class CategoryDetailsSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name',  'image', "products"]