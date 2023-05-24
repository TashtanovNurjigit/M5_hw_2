from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from product.models import Category, Product, Review
from product import serializers


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = serializers.CategoryListSerializer(categories, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data

        category = Category.objects.create(
            name=data.get('name')
        )
        return Response(data=serializers.CategoryListSerializer(category).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'Category not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CategoryDetailSerializer(category, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data

        category.name = data.get('name')

        category.save()

        return Response(data=serializers.CategoryDetailSerializer(category).data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = serializers.ProductListSerializer(products, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data

        product = Product.objects.create(
            title=data.get('title'),
            price=data.get('price'),
            description=data.get('description'),
            category_id=data.get('category_id')
        )

        return Response(data=serializers.ProductListSerializer(product).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ProductDetailSerializer(product, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data

        product.title = data.get('title')
        product.description = data.get('description')
        product.price = data.get('price')
        product.category_id = data.get('category_id')

        product.save()
        return Response(data=serializers.ProductDetailSerializer(product).data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = serializers.ReviewListSerializer(reviews, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data

        review = Review.objects.create(
            product_id=data.get('product_id'),
            text=data.get('text'),
            stars=data.get('stars')
        )

        return Response(data=serializers.ReviewListSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ProductDetailSerializer(review, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data

        review.text = data.get('text')
        review.product_id = data.get('product_id')
        review.stars = data.get('stars')

        review.save()
        return Response(serializers.ReviewDetailSerializer(review).data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def product_reviews_api_view(request):
    product = Product.objects.all()
    serializer = serializers.ProductReviewSerializer(product, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
