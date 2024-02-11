from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pro_id', 'pro_name', 'pro_price', 'pro_desc', 'pro_img']

admin.site.register(Product, ProductAdmin)