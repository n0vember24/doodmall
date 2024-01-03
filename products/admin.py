from django.contrib import admin
from django.db.models import JSONField
from jsoneditor.forms import JSONEditor
from parler.admin import TranslatableAdmin

from products.models import Country, Brand, Product, Category, SubCategory, Review, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Country)
class CountryAdmin(TranslatableAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    readonly_fields = ('slug',)


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
    list_display = ('title', 'is_exists', 'updated_at')
    search_fields = ('translations__title', 'translations__description')
    list_filter = ('category', 'is_exists', 'created_at', 'updated_at')
    readonly_fields = ('is_exists', 'slug', 'created_at', 'updated_at')
    inlines = (ProductImageInline,)
    formfield_overrides = {
        JSONField: {
            "widget": JSONEditor(
                init_options={
                    "mode": "view",
                    "modes": [
                        "view",
                        "code",
                        "tree"
                    ]
                },
                ace_options={
                    "readOnly": True
                },
            )
        }
    }


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
