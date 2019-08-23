from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from shop.models import Shop


class Cashbox(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, default=None)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True, default=None)
    cashier = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = 'Касса'
        verbose_name_plural = 'Кассы'

    def __str__(self):
        return self.name
