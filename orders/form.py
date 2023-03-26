from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    email = forms.EmailInput(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Страна, Город, Улица, Дом, Квартира'
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')