from django.contrib import admin
from .models import Category,Product,cart,Admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

#fields = list(UserAdmin.fieldsets)
#fields[0] = (None, {'fields': ('username', 'password')})
#UserAdmin.fieldsets = tuple(fields)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(cart)
admin.site.register(Admin)
