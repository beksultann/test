from django.db import models


class Report(models.Model):
    opened_cash = models.DateTimeField(auto_now_add=True)
    closed_cash = models.DateTimeField(blank=True, null=True)
    cashier = models.CharField(max_length=30, blank=True, null=True)
    cash = models.CharField(max_length=30, blank=True, null=True)
    shop = models.CharField(max_length=30, blank=True, null=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    total_sold_product = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.cashier
