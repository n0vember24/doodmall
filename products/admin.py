from django.contrib import admin

from products.models import Country, Brand, Product, Category, SubCategory, Review


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
