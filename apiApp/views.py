from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cart, CartItem, Category, Product
from .serializers import (
    CartSerializer,
    CartStatSerializer,
    CategoryDetailsSerializer,
    CategoryListSerializer,
    ProductDetailSerializer,
    ProductListSerializer,
)

# Create your views here.


@api_view(["GET"])
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)


@api_view(["GET"])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def category_detail(request, slug):
    categories = Category.objects.get(slug=slug)
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_to_cart(request):
    cart_code = request.data.get("cart_code")
    product_id = request.data.get("product_id")

    cart, created = Cart.objects.get_or_create(cart_code=cart_code)
    product = Product.objects.get(id=product_id)

    cartItem, created = CartItem.objects.get_or_create(product=product, cart=cart)
    cartItem.quantity = 1
    cartItem.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data)


@api_view(["PUT"])
def update_cartitem_quantity(request, slug):
    cartitem_id = request.data.get("item_id")
    quantity = request.data.get("quantity")
    cartitem = CartItem.objects.get(id=cartitem_id)
    cartitem_id.quantity = quantity
    cartitem.save()

    serializer = CartStatSerializer(cartitem)
    return Response(
        {"data": serializer.data, "message": "Cart Item updated successfully"}
    )
