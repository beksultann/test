from django.contrib import admin

from product.models import *
from shop.models import CostsOfShop


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'suppliers_name', 'selling_price', 'quantity')
    list_per_page = 50
    list_display_links = ['name']
    list_filter = ['quantity', 'name']
    list_editable = ['selling_price']
    search_fields = ['name']


class CartFilter(admin.ModelAdmin):
    search_fields = ['author', ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart, CartFilter)
admin.site.register(CostsOfShop)
