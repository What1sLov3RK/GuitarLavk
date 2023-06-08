from django.contrib import admin
from .models import Product, Categories, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand", "model", "price")}
    search_fields = ('brand', 'model')
    list_display = ('type', 'brand', 'model', 'price', 'quantity', 'picture')
    list_editable = ('price', 'quantity')



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'price')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
    list_display_links = ('category',)

