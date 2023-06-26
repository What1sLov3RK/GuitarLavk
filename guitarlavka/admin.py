from django.contrib import admin
from .models import Product, Categories, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand", "model", "price")}
    search_fields = ('brand', 'model')
    list_display = ('type', 'brand', 'model', 'price', 'quantity', 'picture')
    list_editable = ('price', 'quantity')


@admin.register(OrderItem)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('user', 'model')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'price')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'order_items':
            order_id = request.resolver_match.kwargs.get('object_id')
            kwargs['queryset'] = OrderItem.objects.filter(order__id=order_id)

        return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
    list_display_links = ('category',)

