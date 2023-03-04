from django.urls import path

from products.views import basket_add, basket_remove, ProductsListView  #, products

app_name = 'products'

urlpatterns = [
    # path('products/', products_view, name='products'),
    path('', ProductsListView.as_view(), name='index'),
    # path('', products, name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
