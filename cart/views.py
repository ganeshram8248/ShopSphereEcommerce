from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import CartItem
from .models import Cart

from products.models import Product



@login_required
def cart_detail(request):


    cart=Cart.objects.get(

    user=request.user

    )


    items=CartItem.objects.filter(

    cart=cart

    )


    total=sum(

    item.total_price()

    for item in items

    )



    return render(

    request,

    'cart.html',

    {

    'cart_items':items,

    'total':total

    }

    )





@login_required
def add_cart(

request,

id

):


    product=Product.objects.get(

    id=id

    )


    cart=Cart.objects.get(

    user=request.user

    )


    item,created=CartItem.objects.get_or_create(

    cart=cart,

    product=product

    )



    if not created:

        item.quantity+=1

        item.save()



    return redirect(

    'cart'

    )





@login_required
def remove_cart(

request,

id

):


    item=CartItem.objects.get(

    id=id

    )


    item.delete()


    return redirect(

    'cart'

    )