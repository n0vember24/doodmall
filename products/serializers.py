from rest_framework.serializers import ModelSerializer

from products.models import Product, Category, SubCategory, ProductImage, Country, Brand, Review


class ProductSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product


class CategorySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class SubCategorySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = SubCategory


class ProductImageSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductImage


class CountrySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Country


class BrandSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Brand


class ReviewSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Review
