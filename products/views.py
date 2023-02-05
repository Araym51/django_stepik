from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = {
            'title': 'django Store',
            'is_promotion': False,
        }
        return context


def products_view(request):
    return render(request, 'products/products.html')
