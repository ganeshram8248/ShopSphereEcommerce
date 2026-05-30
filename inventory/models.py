from django.db import models
from products.models import Product


class StockMovement(models.Model):

    product=models.ForeignKey(

        Product,

        on_delete=models.CASCADE

    )


    quantity=models.IntegerField(
        default=0
    )


    movement_type=models.CharField(

        max_length=20,

        choices=[

        ('purchase','Purchase'),

        ('sale','Sale'),

        ('return','Return'),

        ('adjustment','Adjustment')

        ]

    )


    created_at=models.DateTimeField(

        auto_now_add=True

    )


    def __str__(self):

        return self.product.name