from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import ListView, TemplateView
from django.core.cache import cache

from common.views import TitleMixin

from .models import Basket, Product, ProductCategory

# Create your views here.


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(TitleMixin, ListView):
    template_name = 'products/products.html'
    model = Product
    paginate_by = 3  # итерируемся по page_obj!
    title = 'Store - каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        categories = cache.get('categories')
        if not categories:
            context['products_category'] = ProductCategory.objects.all()
            cache.set('products_category', context['products_category'], 30)
        else:
            context['products_category'] = categories
        return context


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
