from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomerProfile
from orders.models import Order
from userwishlist.models import Wishlist   # ✅ FIXED# If you have wishlist model, uncomment below:
# from wishlist.models import Wishlist


@login_required
def profile(request):

    profile, created = CustomerProfile.objects.get_or_create(
        user=request.user
    )

    orders = Order.objects.filter(user=request.user)
    wishlist = Wishlist.objects.filter(user=request.user)

    total_spent = sum(
        float(o.total_amount or 0)
        for o in orders
    )

    # SAVE PROFILE EDIT
    if request.method == "POST":
        profile.phone = request.POST.get("phone")
        profile.address = request.POST.get("address")
        profile.save()
        return redirect("profile")

    context = {
        "profile": profile,
        "orders_count": orders.count(),
        "total_spent": total_spent,
        "wishlist_count": wishlist.count(),
    }

    return render(request, "profile.html", context)
# =========================
# DASHBOARD VIEW
# =========================@login_required
def dashboard(request):

    orders = Order.objects.filter(user=request.user)

    total_spent = sum(
        float(getattr(order, "total_amount", 0) or 0)
        for order in orders
    )

    return render(request, "dashboard.html", {
        "orders_count": orders.count(),
        "total_spent": total_spent,
        "recent_orders": orders.order_by("-created_at")[:5],
    })
# =========================
# CUSTOMERS LIST (STAFF ONLY)
# =========================
@login_required
def customers_list(request):

    if not request.user.is_staff:
        return render(request, "dashboard.html")

    customers = CustomerProfile.objects.select_related("user").all()

    return render(request, "customers.html", {
        "customers": customers
    })