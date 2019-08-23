from django import forms

from counterparties.models import Supplier, Customer, Employees


class SupplierForm(forms.ModelForm):
    organization = forms.CharField(max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'input-text', 'type': 'text',
                                                                 'placeholder': 'Поиск по организации по наименованию, ИНН или ОГРН'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text', 'type': 'text'}),
                           required=False)
    phone_number = forms.CharField(max_length=15,
                                   widget=forms.TextInput(attrs={'class': 'input__input', 'type': 'text'}),
                                   required=False)
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input__input', 'type': 'text'}),
                            required=False)
    web_page = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input-text', 'type': 'text'}),
                               required=False)
    requisite_organization_name = forms.CharField(max_length=30,
                                                  widget=forms.TextInput(attrs={'class': 'input__input', 'type': 'text',
                                                                                'placeholder': 'Наименование реквизита'}),
                                                  required=False)
    requisite_organization_number = forms.CharField(max_length=30,
                                                    widget=forms.TextInput(
                                                        attrs={'class': 'input-text', 'type': 'text',
                                                               'placeholder': 'Номер реквизита'}), required=False)
    bank_requisite = forms.CharField(max_length=18,
                                     widget=forms.TextInput(attrs={'class': 'input-text', 'type': 'text'}),
                                     required=False)
    legal_address = forms.CharField(max_length=50,
                                    widget=forms.TextInput(
                                        attrs={'class': 'input-text input-text--big', 'rows': '10'}), required=False)
    actual_address = forms.CharField(max_length=50,
                                     widget=forms.TextInput(
                                         attrs={'class': 'input-text input-text--big', 'type': 'text'}), required=False)
    comment = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'textarea', 'type': 'text'}),
                              required=False)

    class Meta:
        model = Supplier
        fields = (
            'organization', 'name', 'phone_number', 'email', 'web_page', 'requisite_organization_name',
            'requisite_organization_number', 'bank_requisite', 'legal_address',
            'actual_address',
            'comment')


CHOICES = [('Male', 'Мужской'),
           ('Female', 'Женский')]


class CustomersForm(forms.ModelForm):
    sex = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    address = forms.CharField(max_length=50,
                              widget=forms.TextInput(
                                  attrs={'class': 'input-text input-text--big', 'type': 'text'}), required=False)
    comment = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'textarea', 'type': 'text'}),
                              required=False)

    class Meta:
        model = Customer
        fields = (
            'name', 'phone_number', 'email', 'discount', 'discount_card',
            'date_of_birth', 'sex', 'address', 'comment')


class EmployeesForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    sex = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    pay = forms.CharField(max_length=10,
                          widget=forms.TextInput(attrs={'class': 'input-text'}))

    class Meta:
        model = Employees
        fields = (
            'name', 'phone_number', 'email',
            'date_of_birth', 'sex', 'address', 'comment', 'pay')
