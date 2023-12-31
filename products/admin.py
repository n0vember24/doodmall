from django.contrib import admin
from parler.admin import TranslatableAdmin

from products.models import Country, Brand, Product, Category, SubCategory, Review, ProductImage


@admin.register(Country)
class CountryAdmin(TranslatableAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(TranslatableAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(TranslatableAdmin):
    pass


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
