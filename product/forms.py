from django import forms

from cashbox.models import Shop
from counterparties.models import Supplier
from product.models import Product, Category


class ProductsForm(forms.ModelForm):
    suppliers_name = forms.ModelChoiceField(queryset=Supplier.objects.all(),
                                            widget=forms.Select(attrs={'class': 'my-select'}))

    categories_name = forms.ModelChoiceField(queryset=Category.objects.all(),
                                             widget=forms.Select(attrs={'class': 'my-select'}))

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    quantity = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    barcode = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input-text'}))
    image = forms.ImageField(required=False)
    unit = forms.CharField(max_length=10,
                           widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'шт/кг/л'}))
    comment = forms.CharField(max_length=300,
                              widget=forms.Textarea(attrs={'class': 'textarea', 'rows': '10'}), required=False)
    purchase_price = forms.CharField(max_length=10,
                                     widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Сом'}))
    selling_price = forms.CharField(max_length=10,
                                    widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Сом'}),
                                    required=False)
    discount = forms.CharField(max_length=10,
                               widget=forms.TextInput(attrs={'class': 'input-text', 'value': '0'}),
                               required=False)
    vat = forms.CharField(max_length=10,
                          widget=forms.TextInput(attrs={'class': 'input-text', 'value': '0'}),
                          required=False)
    shop = forms.ModelChoiceField(queryset=Shop.objects.all(),
                                  widget=forms.Select(attrs={'class': 'my-select'}))

    class Meta:
        model = Product
        fields = (
            'suppliers_name', 'categories_name', 'name', 'quantity', 'barcode', 'image', 'unit', 'comment',
            'purchase_price',
            'selling_price',
            'discount',
            'vat', 'shop',)


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))

    class Meta:
        model = Category
        fields = (
            'name',)
