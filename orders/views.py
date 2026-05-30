from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Order
from core.views import PRODUCT_LIST
from django.http import JsonResponse


@login_required
def cancel_order(request,id):

    try:

        order = Order.objects.get(

            id=id,

            user=request.user

        )


        order.status="Cancelled"


        order.save()


        return JsonResponse(

            {

                "success":True,

                "status":"Cancelled"

            }

        )


    except:

        return JsonResponse(

            {

                "success":False

            }

        )


@login_required
def all_orders(request):

    profile = request.user.profile


    if profile.role != "admin":

        return redirect("/")


    orders = Order.objects.all()


    return render(

        request,

        "all_orders.html",

        {

            "orders": orders

        }

    )
@login_required
def orders_list(request):

    orders=Order.objects.filter(

        user=request.user

    )


    return render(

        request,

        'orders.html',

        {

            'orders':orders

        }

    )
@login_required
def buy_now(

request,

id

):


    product=None


    for p in PRODUCT_LIST:

        if p["id"]==id:

            product=p



    if request.method=="POST":


        Order.objects.create(

            user=request.user,

            product_name=

            product["name"],

            price=

            product["price"],

            phone=

            request.POST["phone"],

            address=

            request.POST["address"]

        )


        return redirect(

        "orders_success"

        )


    return render(

    request,

    "buy_now.html",

    {

    "product":product

    }

    )
