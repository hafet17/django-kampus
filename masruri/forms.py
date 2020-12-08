from django import forms
from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'custumer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'custumer': 'Konsumen',
            'product': 'Produk',
            'status': 'Status Order',
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        paginate_by = 6
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nama Produk',
            'price': 'Harga Produk',
            'category': 'Kategori Produk',
            'description': 'Deskripsi',
            'tag': 'Tag',
        }
