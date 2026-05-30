from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):

    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE

    )


    shop_name = models.CharField(

        max_length=200

    )


    phone = models.CharField(

        max_length=15,

        blank=True

    )


    email = models.EmailField(

        blank=True

    )


    address = models.TextField(

        blank=True

    )


    total_sales = models.IntegerField(

        default=0

    )


    total_orders = models.IntegerField(

        default=0

    )


    total_products = models.IntegerField(

        default=0

    )


    verified = models.BooleanField(

        default=False

    )


    def __str__(self):

        return self.shop_name