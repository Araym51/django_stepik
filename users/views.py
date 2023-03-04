from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User
from common.views import TitleMixin


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(SuccessMessageMixin, TitleMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация успешна!'
    title = 'Store - регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'Store - личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context
