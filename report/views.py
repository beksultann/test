from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from report.models import Report


@method_decorator(login_required, name='dispatch')
class ReportView(TemplateView):
    template_name = 'report/reports.html'

    def get(self, request, *args, **kwargs):
        reports = Report.objects.filter(opened_cash__contains=date.today())
        total_price = 0
        total_sold_product = 0
        today = date.today()
        for report in reports:
            total_price += float(report.total_price)
            total_sold_product += int(report.total_sold_product)
        print(total_price)
        print(total_sold_product)
        return render(request, self.template_name, context={
            "total_price": total_price,
            "total_sold_product": total_sold_product,
            "today": today,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={

        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReportView, self).dispatch(*args, **kwargs)
