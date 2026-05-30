from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import CustomerProfile
from orders.models import Order
from cart.models import CartItem


@login_required
def dashboard(request):


    orders=Order.objects.filter(

    user=request.user

    )



    cart=CartItem.objects.filter(

    cart__user=request.user

    )




    spent=sum(

    order.price

    for order in orders

    )




    return render(

    request,

    'dashboard.html',

    {

    'orders':orders,

    'order_count':

    orders.count(),




    'cart_count':

    cart.count(),




    'spent':

    spent

    }

    )





@login_required
def customers_list(

request

):


    customers=CustomerProfile.objects.all()


    return render(

    request,

    'customers.html',

    {

    'customers':

    customers

    }

    )