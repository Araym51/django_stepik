from django.urls import path

from products.views import basket_add, basket_remove, ProductsView, products

app_name = 'products'

urlpatterns = [
    # path('products/', products_view, name='products'),
    # path('', ProductsView.as_view(), name='index'),
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
