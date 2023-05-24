from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from product.models import Category, Product, Review
from product import serializers


@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    serializer = serializers.CategoryListSerializer(categories, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Category not found!'}, status=status.HTTP_404_NOT_FOUND)

    serializer = serializers.CategoryDetailSerializer(category, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    serializer = serializers.ProductListSerializer(products, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.ProductDetailSerializer(product, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = serializers.ReviewListSerializer(reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = serializers.ProductDetailSerializer(review, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_reviews_api_view(request):
    product = Product.objects.all()
    serializer = serializers.ProductReviewSerializer(product, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
