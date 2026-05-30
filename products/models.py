from django.db import models


class Product(models.Model):

    name = models.CharField(
        max_length=200
    )

    price = models.IntegerField()

    image = models.ImageField(
        upload_to="products/"
    )

    description = models.TextField()

    rating = models.FloatField(
        default=4.5
    )

    stock = models.IntegerField(
        default=10
    )

    category = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.name