from django.views.generic.edit import CreateView

from orders.form import OrderForm
# Create your views here.

class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
