from django.contrib.auth.decorators import login_required
from .models import Profile
from orders.models import Order
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

@login_required
def profile(request):

    profile=Profile.objects.get(

        user=request.user
    )


    if request.method=="POST":

        profile.phone=\
        request.POST["phone"]

        profile.address=\
        request.POST["address"]

        profile.save()



    orders=Order.objects.filter(

        user=request.user
    )


    total_spent=sum(

        order.price

        for order in orders
    )


    context={

        "profile":profile,

        "orders_count":

        orders.count(),

        "total_spent":

        total_spent,

    }



    if profile.role=="admin":

        return render(

        request,

        "admin_profile.html",

        context

        )


    return render(

    request,

    "profile.html",

    context

    )
def login_page(request):


    if request.method=="POST":


        email= request.POST["email"]


        password=request.POST["password"]



        try:

            user_obj=User.objects.get(

            email=email

            )


            user=authenticate(

            username=user_obj.username,

            password=password

            )


            if user:


                login(

                request,

                user

                )


                return redirect(

                "/profile"

                )


        except:

            pass


        return render(

        request,

        "login.html",

        {

        "error":

        "Invalid Login"

        }

        )



    return render(

    request,

    "login.html"

    )





def register_page(request):


    if request.method=="POST":


        username=request.POST["username"]


        email=request.POST["email"]


        password=request.POST["password"]



        if User.objects.filter(

        email=email

        ).exists():


            return render(

            request,

            "register.html",

            {

            "error":

            "Email Exists"

            }

            )




        user=User.objects.create_user(

        username=username,

        email=email,

        password=password

        )


        user.save()



        return redirect(

        "/login"

        )



    return render(

    request,

    "register.html"

    )





def logout_page(request):


    logout(

    request

    )


    return redirect(

    "/login"

    )