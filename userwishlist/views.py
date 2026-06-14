from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product


# =========================
# WISHLIST PAGE
# =========================
@login_required
def wishlist_page(request):
    items = Wishlist.objects.filter(user=request.user)

    return render(request, "wishlist.html", {
        "items": items,
        "wishlist_count": items.count()
    })


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("wishlist")

# =========================
# REMOVE FROM WISHLIST (NEW - IMPORTANT)
# =========================
@login_required
def remove_from_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.filter(
        user=request.user,
        product=product
    ).delete()

    return redirect("wishlist")