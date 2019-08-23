from decimal import Decimal
from time import timezone

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.core.validators import MinValueValidator
from django.db import models

from shop.models import Shop
from counterparties.models import Supplier, Customer


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Катерогия'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    suppliers_name = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True, default=None)
    categories_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    quantity = models.DecimalField(max_digits=20, decimal_places=0, blank=False, null=False, default=0.00)
    barcode = models.CharField(max_length=50, blank=True, null=True, default=None, unique=True)
    image = models.ImageField(upload_to='Image_of_products', default='Image_of_products/foto.png')
    unit = models.CharField(max_length=10, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True, default=None)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    markup = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    discount = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    vat = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True, default=None)
    history = AuditlogHistoryField()

    # counter = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.markup = self.selling_price - self.purchase_price
        self.selling_price = self.selling_price - self.discount
        super(Product, self).save(*args, **kwargs)


auditlog.register(Product)


class Cart(models.Model):
    author = models.CharField(max_length=30, blank=True, null=True)
    customer = models.CharField(max_length=30, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    get_price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    remaining_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    total_product = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return '№' + str(self.id)

    def save(self, *args, **kwargs):
        if float(self.total_price) <= float(self.get_price):
            self.remaining_amount = 0
            self.get_price = self.total_price
        else:
            self.remaining_amount = float(self.total_price) - float(self.get_price)
        super(Cart, self).save(*args, **kwargs)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"

    def __str__(self):
        return self.product.name
