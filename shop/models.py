from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, default=None)
    image = models.FileField(upload_to='Shops_images', blank=True, null=True)
    address = models.TextField(blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class CostsOfShop(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True, default=None)
    money = models.IntegerField(blank=False, null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return self.title
