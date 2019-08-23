from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib import messages

from counterparties.forms import CustomersForm, EmployeesForm
from counterparties.models import Employees
from shop.forms import ShopForm
from shop.models import Shop
from user.forms import UserRegisterForm


@method_decorator(login_required, name='dispatch')
class ShopView(TemplateView):
    template_name = 'shop/shops.html'

    def get(self, request, *args, **kwargs):
        shops = Shop.objects.all()
        form = ShopForm()
        return render(request, self.template_name, context={
            'shops': shops,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = ShopForm(request.POST or None, request.FILES or None)
        shops = Shop.objects.all()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('shops')
        return render(request, self.template_name, context={
            'form': form,
            'shops': shops,
        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShopView, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class EmployeesView(TemplateView):
    template_name = 'shop/employees.html'

    def get(self, request, *args, **kwargs):
        cashiers = User.objects.all()
        employees = Employees.objects.all()
        users = User.objects.all().select_related('Profile')
        form = UserRegisterForm()
        form2 = EmployeesForm()
        return render(request, self.template_name, context={
            'cashiers': cashiers,
            'form': form,
            'users': users,
            'form2': form2,
            'employees': employees,

        })

    def post(self, request, *args, **kwargs):
        users = User.objects.all().select_related('Profile')
        form = UserRegisterForm(request.POST)
        form2 = EmployeesForm(request.POST, request.FILES)

        if form2.is_valid():
            form2.save()
            return redirect('employees')
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('employees')
        else:
            messages.success(request, f'Your account has not been created! Please try again!')
        return render(request, self.template_name, context={
            'form': form,
            'users': users,
            'form2': form2,
        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EmployeesView, self).dispatch(*args, **kwargs)


def delete_users(request, id):
    first = User.objects.get(id=id)
    first.delete()
    return redirect('employees')


def delete_employees(request, id):
    first = Employees.objects.get(id=id)
    first.delete()
    return redirect('employees')


def delete_shop(request, id):
    shop = Shop.objects.get(id=id)
    shop.delete()
    return redirect('shops')
