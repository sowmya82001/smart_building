from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Supplier, Order, Inventory

# Home Page
def home(request):
    return render(request, 'procurement/home.html')

# Dashboard View
@login_required
def dashboard(request):
    return render(request, 'procurement/dashboard.html')

# Supplier List View
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'procurement/suppliers.html', {'suppliers': suppliers})

# Order List View
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'procurement/orders.html', {'orders': orders})

# Inventory List View
def inventory_list(request):
    inventory = Inventory.objects.all()
    return render(request, 'procurement/inventory.html', {'inventory': inventory})
