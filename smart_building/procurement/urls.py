from django.urls import path
from .views import home, dashboard, supplier_list, order_list, inventory_list

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('suppliers/', supplier_list, name='supplier_list'),
    path('orders/', order_list, name='order_list'),
    path('inventory/', inventory_list, name='inventory_list'),
]
