from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    phone = models.CharField(max_length=15)
    address = models.TextField()

    status = models.CharField(max_length=20, choices=STATUS, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name