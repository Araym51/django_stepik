from django.contrib import admin
from products.models import ProductCategory, Product, Basket
# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ( 'image', ('name', 'category'),  'description', ('price', 'quantity'))
    readonly_fields = ('name',)
    search_fields = ('name',)
    ordering = ('price',)  # ('-price',) сортировка в обратном порядке


# для TabularInline не используется декоратор админа
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
