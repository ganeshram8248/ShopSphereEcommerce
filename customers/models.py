from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):

    ROLE=(
        ('customer','Customer'),
        ('seller','Seller')
    )


    user=models.OneToOneField(

        User,

        on_delete=models.CASCADE

    )


    phone=models.CharField(

        max_length=15,

        blank=True

    )


    address=models.TextField(

        blank=True

    )


    role=models.CharField(

        max_length=20,

        choices=ROLE,

        default='customer'

    )


    def __str__(self):

        return self.user.username