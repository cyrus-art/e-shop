from django.db import models

class Login(models.Model):
    user_name = models.CharField(max_length=100, default="")  # Field for user name
    phone_number = models.CharField(max_length=20, default="")  # Use CharField for phone number

    def __str__(self):
        return self.user_name  # Return user_name when the object is printed

class Iteam(models.Model):
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=200, decimal_places=2)
    user_name = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} for {self.user_name}"


class Customer(models.Model):
    name = models.CharField(max_length=100)  # Increased max_length for name
    mail = models.EmailField(max_length=254, unique=True)
    message = models.TextField()  # Removed default="" to keep it clean

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"