from rest_framework.serializers import ModelSerializer

from product.models import Category, Product, Review


class CategoryListSerializers(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializers(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializers(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'price')


class ProductDetailSerializers(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ReviewListSerializers(ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'text')


class ReviewDetailSerializers(ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
