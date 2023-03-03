from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import ProductCategory, Product, Basket
from users.models import User

# Create your views here.


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'django Store'
        return context


class ProductsView(ListView):
    template_name = 'products/products.html'
    title = 'Catalog'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['products_category'] = ProductCategory.objects.all()
        return context


def products(request, category_id=None, page_number=1):
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(product, per_page)
    products_paginator = paginator.page(page_number)
    context = {
        'title': 'Store - каталог',
        'products_category': ProductCategory.objects.all(),
        'product_list': products_paginator,
    }
    return render(request, 'products/products.html', context)


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
