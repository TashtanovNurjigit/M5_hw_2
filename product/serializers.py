from rest_framework.serializers import ModelSerializer

from product.models import Category, Product, Review


class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = 'id name products_count'.split()


class CategoryDetailSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class ProductDetailSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ReviewListSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'text', 'stars')


class ReviewDetailSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ProductReviewSerializer(ModelSerializer):
    product_reviews = ReviewListSerializer(many=True)

    class Meta:
        model = Product
        fields = 'title product_reviews rating'.split()
