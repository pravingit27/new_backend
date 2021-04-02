from django.contrib import admin
from .models import Category,Product,cart
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(cart)
