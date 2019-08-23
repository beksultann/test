import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from cashbox.models import Cashbox
from counterparties.forms import CustomersForm, EmployeesForm
from counterparties.models import Customer, Employees
from product.models import Product, Category, Cart, CartProduct
from report.models import Report
from datetime import datetime

from shop.forms import CostsOfShopForm
from shop.models import Shop


@method_decorator(login_required, name='dispatch')
class CashierView(TemplateView):
    template_name = 'cashier/cash_interface.html'

    def get(self, request, *args, **kwargs):

        search_query = request.GET.get('search', '')
        filter_product = request.GET.get('filter_product', '')
        categories = Category.objects.all()
        products = Product.objects.all()
        form = CustomersForm()
        form_cost = CostsOfShopForm()
        customers = Customer.objects.all()
        employees = Employees.objects.all()
        if filter_product:
            products = products.filter(categories_name__name=filter_product)
        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) | Q(barcode__icontains=search_query) | Q(
                    id__icontains=search_query))

        return render(request, self.template_name, context={
            'products': products,
            'categories': categories,
            'form': form,
            'customers': customers,
            'form_cost': form_cost,
            'employees': employees,
            # 'cart': cart,
        })

    def post(self, request, *args, **kwargs):
        products = Product.objects.all()
        employees = Employees.objects.all()
        form = CustomersForm(request.POST, request.FILES)
        form_cost = CostsOfShopForm(request.POST, request.FILES)
        customers = Customer.objects.all()
        if form.is_valid():
            form.save()
            messages.info(request, 'Клиент создан!')
            return redirect('cashier_interface')
        if form_cost.is_valid():
            form_cost.save()
            messages.info(request, 'Расходы!')
            return redirect('cashier_interface')
        return render(request, self.template_name, context={
            'products': products,
            'form': form,
            'customers': customers,
            'form_cost': form_cost,
            'employees': employees,
        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CashierView, self).dispatch(*args, **kwargs)


def employees_prepayment(request):
    employees = request.POST.get('employees_name')
    prepayment = request.POST.get('prepayment')
    empl = Employees.objects.get(name=employees)
    empl.prepayment = int(prepayment)
    empl.remains = empl.pay - int(prepayment)
    empl.save()
    messages.info(request, empl.name + ' получил аванс в размере ' + prepayment + ' сом')
    return redirect('cashier_interface')


def log_cash(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    shops = Shop.objects.all()
    cashboxes = Cashbox.objects.all()

    return render(request, 'cashier/log_cash.html', context={
        'products': products,
        'categories': categories,
        'shops': shops,
        'cashboxes': cashboxes,
    })


def cashier_save(request):
    cash = request.POST.get('cash_name')
    shop = request.POST.get('shop_name')
    if cash and shop:
        report = Report()
        report.cashier = request.user.username
        report.cash = cash
        report.shop = shop
        report.save()
        return redirect('cashier_interface')
    else:
        return redirect('log_cash')


def report_save_of_cashier(request):
    reports = Report.objects.all()
    reports = reports.filter(cashier=request.user.username)
    report = reports.order_by('-opened_cash')[0]
    report.closed_cash = datetime.now()
    report.save()
    total_product = 0
    total_price = 0
    products = Cart.objects.all()
    products = products.filter(author=report)
    products = products.filter(created_date__gte=report.opened_cash)
    for product in products:
        total_product += product.total_product
        total_price += product.total_price
    report.total_price = total_price
    report.total_sold_product = total_product
    report.save()
    return redirect('logout')


def save_to_database(request):
    products = request.session['product']
    customer_name = request.POST.get('customer_name')
    get_price = request.POST.get('get_price')
    cart = Cart()
    cart.author = request.user.username
    cart.customer = customer_name
    cart.get_price = get_price
    cart.save()

    total = 0
    total_qty = 0
    for product in products:
        cart_item = CartProduct()
        item = Product.objects.get(pk=product['pk'])
        cart_item.product = item
        cart_item.qty = product['counter']
        item.quantity = item.quantity - product['counter']
        item.save()
        cart_item.cart = cart
        cart_item.save()
        total = total + float(product['fields']['selling_price']) * int(product['counter'])
        total_qty += product['counter']
    cart.total_price = total
    cart.total_product = total_qty
    cart.save()
    messages.info(request, 'Продукт продан!')
    return redirect('clear_session')


def clear_session(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        print(key)
        if key == 'product':
            del request.session[key]
    return redirect('cashier_interface')


def add_to_cart(request, id):
    records = []
    total_price = 0
    one_price = Product.objects.get(id=id)
    customers = Customer.objects.all()
    if "product" in request.session:
        product = Product.objects.filter(id=id)
        json_product = serializers.serialize('json', product)
        json_product = json.loads(json_product)[0]
        json_product['counter'] = 1
        json_product['one_price'] = float(one_price.selling_price)
        check = False
        old_products = [request.session['product']]
        for item in old_products[0]:
            try:
                if item['pk'] != json_product['pk']:
                    records.append(item)
                else:
                    item['counter'] += 1
                    item['one_price'] = float(one_price.selling_price) * item['counter']
                    records.append(item)
                    check = True
            except TypeError:
                records.append(item)

        if not check:
            records.append(json_product)
        request.session['product'] = records
    else:
        product = Product.objects.filter(id=id)
        json_product = serializers.serialize('json', product)
        json_product = json.loads(json_product)[0]
        json_product['counter'] = 1
        json_product['one_price'] = float(one_price.selling_price)
        records.append(json_product)
        request.session['product'] = records
    for total in request.session['product']:
        total_price += total['one_price']

    products = Product.objects.all()
    context = {
        'products': products,
        'records': records,
        'total_price': total_price,
        'customers': customers,
    }
    return render(request, 'cashier/cash_interface.html', context)
