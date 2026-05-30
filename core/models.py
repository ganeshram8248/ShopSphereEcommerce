from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    name = models.CharField(
        max_length=200
    )

    price = models.IntegerField()

    image = models.ImageField(
        upload_to='products/'
    )

class Wishlist(models.Model):

    user =models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product_name =models.CharField(
        max_length=200
    )

    price =models.IntegerField()

    image =models.ImageField(
        upload_to="wishlist/"
    )


    def __str__(self):

        return self.product_name