from django import forms

from shop.models import Shop, CostsOfShop


class ShopForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    image = forms.ImageField(required=False)
    address = forms.CharField(max_length=300,
                              widget=forms.Textarea(attrs={'class': 'textarea', 'rows': '10'}), required=False)
    comment = forms.CharField(max_length=300,
                              widget=forms.Textarea(attrs={'class': 'textarea', 'rows': '10'}), required=False)

    class Meta:
        model = Shop
        fields = ('name', 'image', 'address', 'comment',)


class CostsOfShopForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    comment = forms.CharField(max_length=300,
                              widget=forms.Textarea(attrs={'class': 'textarea', 'rows': '10'}), required=False)
    money = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))

    class Meta:
        model = CostsOfShop
        fields = ('title', 'comment', 'money',)
