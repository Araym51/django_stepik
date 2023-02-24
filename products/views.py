from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import ProductCategory, Product
# Create your views here.


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = {
            'title': 'django Store',
            'is_promotion': False,
        }
        return context


# def products_view(request):
#     context = {
#         'title': 'Catalog',
#         'products': Product.objects.all(),
#         'products_category': ProductCategory.objects.all()
#     }
#     return render(request, 'products/products.html', context)


class ProductsView(ListView):
    template_name = 'products/products.html'
    title = 'Catalog'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['products_category'] = ProductCategory.objects.all()
        return context
