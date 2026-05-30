from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from vendors.models import Vendor

from .models import Product


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.products import PRODUCT_LIST
from userwishlist.models import Wishlist
from products.models import Product
from cart.models import CartItem
from cart.models import Cart  
from userprofile.models import Profile
from orders.models import Order

# HOME

def index(request):

    return render(
        request,
        "index.html"
    )

def login_page(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "login.html", {"error": "Fill all fields"})

        try:
            user = User.objects.get(email=email)

            auth_user = authenticate(
                request,
                username=user.username,
                password=password
            )

            if auth_user:
                login(request, auth_user)
                return redirect("/profile/")
            else:
                return render(request, "login.html", {"error": "Invalid password"})

        except User.DoesNotExist:
            return render(request, "login.html", {"error": "Email not registered"})

    return render(request, "login.html")
# LOGOUT

def logout_view(request):

    logout(request)

    return redirect(
        "login"
    )


# REGISTER
def register_page(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "Email already exists"})

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("/login/")

    return render(request, "register.html")

# PRODUCTS

def products(request):

    products = Product.objects.all()

    return render(

        request,

        "products.html",

        {

        "products":

        products

        }

    )


# PRODUCT DETAIL

def product_detail(

        request,

        id

):

    product = get_object_or_404(

        Product,

        id=id

    )


    return render(

        request,

        "product_detail.html",

        {

        "product":

        product

        }

    )


# PROFILE

@login_required
def profile(request):

    profile = Profile.objects.get(

        user=request.user

    )


    orders_count = Order.objects.filter(

        user=request.user

    ).count()



    total_spent = sum(

        Order.objects.filter(

            user=request.user

        ).values_list(

            "price",

            flat=True

        )

    )


    wishlist_count = Wishlist.objects.filter(

        user=request.user

    ).count()


    return render(

        request,

        "profile.html",

        {

        "profile":

        profile,

        "orders_count":

        orders_count,

        "total_spent":

        total_spent,

        "wishlist_count":

        wishlist_count

        }

    )


# CUSTOMER DASHBOARD

@login_required
def customer_dashboard(

        request

):

    orders = Order.objects.filter(

        user=request.user

    )


    cart_count = CartItem.objects.filter(

        cart__user=request.user

    ).count()


    spent = sum(

        o.price

        for o in orders

    )


    return render(

        request,

        "customer_dashboard.html",

        {

        "orders":

        orders,

        "order_count":

        orders.count(),

        "cart_count":

        cart_count,

        "spent":

        spent

        }

    )



# SELLER

@login_required
def seller_dashboard(

        request

):

    if request.user.profile.role != "seller":

        return redirect(

            "home"

        )


    return render(

        request,

        "seller_dashboard.html"

    )


# ORDERS

@login_required
def orders(

        request

):

    orders = Order.objects.filter(

        user=request.user

    )


    return render(

        request,

        "orders.html",

        {

        "orders":

        orders

        }

    )


# ALL ORDERS

@login_required
def all_orders(

        request

):

    if request.user.profile.role != "admin":

        return redirect(

            "orders"

        )


    orders = Order.objects.all()


    return render(

        request,

        "all_orders.html",

        {

        "orders":

        orders

        }

    )


# WISHLIST

@login_required
def wishlist(

        request

):

    items = Wishlist.objects.filter(

        user=request.user

    )


    return render(

        request,

        "wishlist.html",

        {

        "items":

        items

        }

    )


@login_required
def remove_wishlist(

        request,

        id

):

    item = Wishlist.objects.get(

        id=id,

        user=request.user

    )

    item.delete()


    return JsonResponse(

        {

        "message":

        "Removed"

        }

    )


# CART

def cart(request):

    return render(

        request,

        "cart.html"

    )


# INVENTORY

def inventory(request):

    return render(

        request,

        "inventory.html"

    )


@login_required
def orders_list(request):

    orders = Order.objects.filter(user=request.user)

    return render(request, "orders.html", {"orders": orders})


@login_required
def cancel_order(request, id):

    if request.method == "POST":

        try:

            order = Order.objects.get(
                id=id,
                user=request.user
            )

            order.status = "Cancelled"
            order.save()

            return JsonResponse({"success": True})

        except Order.DoesNotExist:

            return JsonResponse({"success": False, "error": "Order not found"})

    return JsonResponse({"success": False, "error": "Invalid request"})

@login_required
def settings_view(request):
    return render(request, "settings.html")


@login_required
def buy_now(request, id):
    
    product = None

    for p in PRODUCT_LIST:
        if p["id"] == id:
            product = p

    if request.method == "POST":

        Order.objects.create(

            user=request.user,
            product_name=product["name"],
            price=product["price"],
            phone=request.POST["phone"],
            address=request.POST["address"]

        )

        return redirect("orders_list")
@login_required(
    login_url="/login/"
)

def checkout(request,id):

    product = get_object_or_404(

        Product,

        id=id

    )


    if request.method=="POST":


        name = request.POST.get(

            "name"

        )


        address = request.POST.get(

            "address"

        )


        phone = request.POST.get(

            "phone"

        )



        order = Order.objects.create(

            user=request.user,

            product=product,

            name=name,

            address=address,

            phone=phone

        )



        vendor = Vendor.objects.filter(

         user=product.user

        ).first()



        if vendor:


            vendor.total_orders += 1


            vendor.total_sales += (

                product.price

            )



            vendor.total_products = (

                Product.objects.filter(

                    user=vendor.user

                ).count()

            )



            vendor.save()



        return redirect(

            "order_success"

        )



    return render(

        request,

        "checkout.html",

        {

        "product":product

        }

    )

def order_success(request):
    return render(request, "order_success.html")

@login_required
def add_to_cart(request, id):

    if request.method == "POST":
        product = Product.objects.get(id=id)

        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})