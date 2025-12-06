from django import forms
from .models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'productName',
            'categoryID',
            'price',
            'productDescript',
            'weight',
            'availability',
            'shipping',
            'productImage',
        ]