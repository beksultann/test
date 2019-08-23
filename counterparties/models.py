from django.utils import timezone

from django.db import models


class Supplier(models.Model):
    organization = models.CharField(max_length=100, blank=True, null=True, default=None)
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=15, blank=True, null=True, default=None)
    email = models.CharField(max_length=30, blank=True, null=True, default=None)
    web_page = models.CharField(max_length=30, blank=True, null=True, default=None)
    requisite_organization_name = models.CharField(max_length=30, blank=True, null=True, default=None)
    requisite_organization_number = models.CharField(max_length=30, blank=True, null=True, default=None)
    bank_requisite = models.CharField(max_length=18, blank=True, null=True, default=None)
    legal_address = models.CharField(max_length=50, blank=True, null=True, default=None)
    actual_address = models.CharField(max_length=50, blank=True, null=True, default=None)
    comment = models.CharField(max_length=300, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.organization


class Customer(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default=None)
    phone_number = models.CharField(max_length=50, blank=True, null=True, default=None)
    email = models.CharField(max_length=30, blank=True, null=True, default=None)
    discount = models.CharField(max_length=10, blank=True, null=True, default=None)
    discount_card = models.CharField(max_length=100, blank=True, null=True, default=None)
    date_of_birth = models.CharField(max_length=15, blank=True, null=True, default=None)
    sex = models.CharField(max_length=10, blank=True, null=True, default=None)
    address = models.CharField(max_length=200, blank=True, null=True, default=None)
    comment = models.CharField(max_length=300, blank=True, null=True, default=None)
    date_of_created = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Employees(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, default=None)
    phone_number = models.CharField(max_length=50, blank=True, null=True, default=None)
    email = models.CharField(max_length=30, blank=True, null=True, default=None)
    date_of_birth = models.CharField(max_length=15, blank=True, null=True, default=None)
    sex = models.CharField(max_length=10, blank=True, null=True, default=None)
    address = models.CharField(max_length=200, blank=True, null=True, default=None)
    comment = models.CharField(max_length=300, blank=True, null=True, default=None)
    pay = models.IntegerField(blank=False, null=False, default=0)
    prepayment = models.IntegerField(blank=False, null=False, default=0)
    remains = models.IntegerField(blank=False, null=False, default=0)
    date_of_created = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.remains = self.pay - self.prepayment
        super(Employees, self).save(*args, **kwargs)
