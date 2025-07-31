from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cart, CartItem, Category, Product, Review
from .serializers import (
    CartSerializer,
    CartStatSerializer,
    CategoryDetailsSerializer,
    CategoryListSerializer,
    ProductDetailSerializer,
    ProductListSerializer,
    ReviewSerializer,
)

User = get_user_model()


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
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailsSerializer(category)

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
def update_cartitem_quantity(request):
    cartitem_id = request.data.get("item_id")
    quantity = request.data.get("quantity")
    quantity = int(quantity)
    cartitem = CartItem.objects.get(id=cartitem_id)
    cartitem.quantity = quantity
    cartitem.save()

    serializer = CartStatSerializer(cartitem.cart)
    return Response(
        {"data": serializer.data, "message": "Cart Item updated successfully"}
    )


@api_view(["POST"])
def add_review(request):

    product_id = request.data.get("product_id")
    email = request.data.get("email")
    rating = request.data.get("rating")
    review_text = request.data.get("review")

    product = Product.objects.get(id=product_id)
    user = User.objects.get(email)

    review = Review.objects.create(
        product=product, user=user, rating=rating, review=review_text
    )
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
