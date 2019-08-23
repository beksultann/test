from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from cashbox.forms import CashboxForm
from cashbox.models import Cashbox
from report.models import Report
from shop.models import Shop


@method_decorator(login_required, name='dispatch')
class CashboxView(TemplateView):
    template_name = 'cashbox/cashbox.html'

    def get(self, request, *args, **kwargs):
        form = CashboxForm()
        cashboxes = Cashbox.objects.all()
        return render(request, self.template_name, context={
            'cashboxes': cashboxes,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = CashboxForm(request.POST, request.FILES)
        cashboxes = Cashbox.objects.all()
        if form.is_valid():
            form.save()
            return redirect('cashbox')
        return render(request, self.template_name, context={
            'form': form,
            'cashboxes': cashboxes,
        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CashboxView, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class ShiftsView(TemplateView):
    template_name = 'cashbox/change.html'

    def get(self, request, *args, **kwargs):
        cashiers = User.objects.all()
        shops = Shop.objects.all()
        select_cashier = request.GET.get('select_cashier')
        select_shop = request.GET.get('select_shop')
        select_cash = request.GET.get('select_cash')
        reports = Report.objects.all()
        cashboxes = Cashbox.objects.all()
        if select_cashier:
            reports = reports.filter(cashier=select_cashier)
        if select_shop:
            reports = reports.filter(shop=select_shop)
        if select_cash:
            reports = reports.filter(cash=select_cash)

        return render(request, self.template_name, context={
            'reports': reports,
            'cashiers': cashiers,
            'shops': shops,
            'cashboxes': cashboxes,
        })

    def post(self, request, *args, **kwargs):
        reports = Report.objects.all
        cashiers = User.objects.all()
        shops = Shop.objects.all()
        cashboxes = Cashbox.objects.all()
        return render(request, self.template_name, context={
            'reports': reports,
            'cashiers': cashiers,
            'shops': shops,
            'cashboxes': cashboxes,
        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ShiftsView, self).dispatch(*args, **kwargs)
