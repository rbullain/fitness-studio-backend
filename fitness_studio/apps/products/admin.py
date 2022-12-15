from django.contrib import admin

from apps.products.models import Product, ProductCategory


@admin.register(ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category__name',)
    list_display = ('name', 'category',)
