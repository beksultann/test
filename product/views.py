import datetime
from auditlog.models import LogEntry
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView

from report.models import Report
from shop.models import Shop
from product.forms import ProductsForm, CategoryForm
from product.models import Product, Category


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'product/index.html'

    def get(self, request, *args, **kwargs):
        shops = Shop.objects.all()
        users = User.objects.all().select_related('Profile')
        search_query = request.GET.get('select_market', '')
        total_price = 0
        products = Report.objects.all()
        for price in products:
            total_price += price.total_price
        average_price = float("{0:.2f}".format(total_price / products.count()))

        if search_query == '':
            purchase_prices = Product.objects.all().values_list(
                'purchase_price', flat=True)
            selling_prices = Product.objects.all().values_list(
                'selling_price', flat=True)
            num = len(list(Product.objects.all()))
            pur_price = 0
            sell_price = 0
            for purchase_price in purchase_prices:
                pur_price += int(purchase_price)
            for selling_price in selling_prices:
                sell_price += int(selling_price)
        else:
            purchase_prices = Product.objects.filter(shop__name=search_query).values_list(
                'purchase_price', flat=True)
            selling_prices = Product.objects.filter(shop__name=search_query).values_list(
                'selling_price', flat=True)
            num = len(list(Product.objects.filter(shop__name=search_query)))
            pur_price = 0
            sell_price = 0
            for purchase_price in purchase_prices:
                pur_price += int(purchase_price)
            for selling_price in selling_prices:
                sell_price += int(selling_price)
        return render(request, self.template_name, context={
            'users': users,
            'num': num,
            'shops': shops,
            'pur_price': pur_price,
            'sell_price': sell_price,
            'total_price': total_price,
            'average_price': average_price,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={

        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ManagerProductsView(TemplateView):
    products_per_page = 50
    template_name = 'manager/product/list.html'

    def get(self, request, *args, **kwargs):
        history = LogEntry.objects.all()
        search_query = request.GET.get('search', None)
        page = request.GET.get('page', 1)
        min_price = request.GET.get('min_price', None)
        max_price = request.GET.get('max_price', None)
        min_quantity = request.GET.get('min_quantity', None)
        max_quantity = request.GET.get('max_quantity', None)
        category = request.GET.get('category', None)
        products = Product.objects.all()
        categories = Category.objects.all()
        form = ProductsForm()
        form_category = CategoryForm()

        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) | Q(barcode__icontains=search_query) | Q(id__icontains=search_query))
        if category:
            products = products.filter(categories_name__name=category)
        if min_price:
            products = products.filter(selling_price__gte=float(min_price))

        if max_price:
            products = products.filter(selling_price__lte=float(max_price))

        if min_quantity:
            products = products.filter(quantity__gte=int(min_quantity))
        if max_quantity:
            products = products.filter(quantity__lte=int(max_quantity))

        paginator = Paginator(products, self.products_per_page)

        result = paginator.get_page(page)

        return render(request, self.template_name, context={
            'products': result,
            'categories': categories,
            'history': history,
            'form': form,
            'form_category': form_category,
        })

    def post(self, request, *args, **kwargs):
        some_var = request.POST.getlist('product')
        products = Product.objects.all()
        form = ProductsForm(request.POST or None, request.FILES or None)
        form_category = CategoryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('manager-products')
        if form_category.is_valid():
            form_category.save()
            return redirect('manager-products')
        for item in some_var:
            instance = Product.objects.get(id=item)
            instance.delete()
        return render(request, self.template_name, context={
            'products': products,
            'form': form,
            'form_category': form_category,
        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ManagerProductsView, self).dispatch(*args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'manager/product/list.html'
    context_object_name = 'manager-products'


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = [
        'suppliers_name', 'categories_name', 'name', 'quantity', 'barcode', 'image', 'unit', 'comment',
        'purchase_price',
        'selling_price',
        'discount', 'shop', ]
    success_url = '/manager/products'

    def form_valid(self, form):
        # form.instance.author = self.request.users
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # if self.request.user == post.author:
        #     return True
        return True


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/manager/products'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
