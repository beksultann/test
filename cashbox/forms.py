from django import forms
from django.contrib.auth.models import User

from cashbox.models import Cashbox, Shop


class CashboxForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    shop = forms.ModelChoiceField(queryset=Shop.objects.all(),
                                  widget=forms.Select(attrs={'class': 'my-select'}))
    cashier = forms.ModelChoiceField(queryset=User.objects.all(),
                                     widget=forms.Select(attrs={'class': 'my-select'}))

    class Meta:
        model = Cashbox
        fields = (
            'name', 'shop', 'cashier')
