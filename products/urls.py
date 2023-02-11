from django.urls import path
from products.views import ProductsView
# from products.views import products_view

app_name = 'products'

urlpatterns = [
    # path('products/', products_view, name='products'),
    path('', ProductsView.as_view(), name='index'),
]
