from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    total = sum(item.total_price() for item in items)

    return render(request, 'cart.html', {
        'cart_items': items,
        'total': total
    })


@login_required
def add_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('cart')


@login_required
def remove_cart(request, id):
    item = get_object_or_404(CartItem, id=id)
    item.delete()
    return redirect('cart')
@login_required
def increase_qty(request, id):
    item = CartItem.objects.get(id=id)
    item.quantity += 1
    item.save()
    return redirect('cart')
@login_required
def decrease_qty(request, id):
    item = CartItem.objects.get(id=id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()  # quantity 1 இருந்தா remove

    return redirect('cart')