from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

class ShopAdmin(ModelAdmin):
    list_display = ('title', 'description', 'imageUrl')
    search_fields = ('title',)

class ProductAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'description', 'amount', 'price', 'images', 'active')}),
        ('Categories', {'fields': ('categories',)}),
    )

admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
# Register your models here.
