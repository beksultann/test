from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, ListView, DetailView, UpdateView, TemplateView
from counterparties.forms import SupplierForm, CustomersForm
from counterparties.models import Supplier, Customer, Employees


@method_decorator(login_required, name='dispatch')
class SupplierView(TemplateView):
    template_name = 'counterparties/supplier.html'

    def get(self, request, *args, **kwargs):
        suppliers = Supplier.objects.all()
        num = len(list(Supplier.objects.all()))
        search_query = request.GET.get('search', '')
        form = SupplierForm()
        if search_query:
            suppliers = Supplier.objects.filter(
                Q(organization__icontains=search_query) | Q(
                    phone_number__contains=search_query))

        return render(request, self.template_name, context={
            'suppliers': suppliers,
            'num': num,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        some_var = request.POST.getlist('supplier')
        suppliers = Supplier.objects.all()
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('supplier')
        for item in some_var:
            instance = Supplier.objects.get(id=item)
            instance.delete()
        return render(request, self.template_name, context={
            'suppliers': suppliers,
            'form': form,
        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SupplierView, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class CustomerView(TemplateView):
    template_name = 'counterparties/customers.html'

    def get(self, request, *args, **kwargs):
        num = Customer.objects.count()
        clients = Customer.objects.all()
        search_customer = request.GET.get('search', '')
        form = CustomersForm()
        if search_customer:
            clients = Customer.objects.filter(
                Q(name__icontains=search_customer))
        return render(request, self.template_name, context={
            'num': num,
            'form': form,
            'clients': clients,


        })

    def post(self, request, *args, **kwargs):
        some_var = request.POST.getlist('customers')
        clients = Customer.objects.all()
        for item in some_var:
            instance = Customer.objects.get(id=item)
            instance.delete()
        return render(request, self.template_name, context={
            'clients': clients,


        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CustomerView, self).dispatch(*args, **kwargs)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'counterparties/supplier.html'
    context_object_name = 'supplier'


class SupplierDetailView(DetailView):
    model = Supplier


class SupplierUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Supplier
    fields = ['organization', 'name', 'phone_number', 'email', 'web_page', 'requisite_organization_name',
              'requisite_organization_number', 'bank_requisite', 'legal_address',
              'actual_address',
              'comment']
    success_url = '/supplier'

    def form_valid(self, form):
        # form.instance.author = self.request.users
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # if self.request.user == post.author:
        #     return True
        return True


class SupplierDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Supplier
    success_url = '/supplier'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
