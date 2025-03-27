from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('contractor', 'Contractor'),
        ('admin', 'Admin'),
        ('supplier', 'Supplier'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='contractor')

# Supplier Model
class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'supplier'})
    company_name = models.CharField(max_length=255)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name

# Order Model
class Order(models.Model):
    contractor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'contractor'})
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered')
    ], default='pending')

    def __str__(self):
        return f"{self.material_name} - {self.status}"

# Inventory Model
class Inventory(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=255)
    stock_level = models.IntegerField()
    reorder_level = models.IntegerField(default=10)

    def is_low_stock(self):
        return self.stock_level < self.reorder_level

    def __str__(self):
        return f"{self.material_name} - {self.stock_level}"
