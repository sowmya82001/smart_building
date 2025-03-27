from django.contrib import admin
from .models import User, Supplier, Order, Inventory

admin.site.register(User)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Inventory)
