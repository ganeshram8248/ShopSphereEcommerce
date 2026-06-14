from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Order
from products.models import Product


# =========================
# USER ORDERS
# =========================
@login_required
def orders_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders.html', {'orders': orders})


# =========================
# BUY NOW (CREATE ORDER)
# =========================
@login_required
def buy_now(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        qty = int(request.POST.get("quantity", 1))

        Order.objects.create(
            user=request.user,
            product=product,
            name=product.name,
            price=product.price,
            quantity=qty,
            phone=request.POST.get("phone"),
            address=request.POST.get("address")
        )

        return redirect('orders_list')

    return render(request, 'buy_now.html', {'product': product})


# =========================
# CANCEL ORDER (AJAX SAFE)
# =========================
@login_required
def cancel_order(request, id):

    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request"})

    try:
        order = Order.objects.get(id=id, user=request.user)
        order.status = "Cancelled"
        order.save()

        return JsonResponse({"success": True})

    except:
        return JsonResponse({"success": False})


# =========================
# ADMIN VIEW
# =========================
@login_required
def all_orders(request):

    if not request.user.is_staff:
        return redirect('/')

    orders = Order.objects.all().order_by('-created_at')

    return render(request, 'all_orders.html', {'orders': orders})