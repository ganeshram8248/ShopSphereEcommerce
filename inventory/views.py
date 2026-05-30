from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product



@login_required
def inventory_list(request):


    products = Product.objects.all()



    total_products = products.count()



    total_stock = sum(

        product.stock

        for product in products

    )



    low_stock = products.filter(

        stock__lt=10,

        stock__gt=0

    ).count()



    out_stock = products.filter(

        stock=0

    ).count()




    available = products.filter(

        stock__gte=10

    ).count()




    context = {

        'products':

        products,


        'total':

        total_products,


        'total_stock':

        total_stock,


        'low':

        low_stock,


        'out':

        out_stock,


        'available':

        available

    }



    return render(

        request,

        'inventory.html',

        context

    )