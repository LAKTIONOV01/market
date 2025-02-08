from django.shortcuts import render, redirect

from carts.models import Cart
from goods.models import Product


# Create your views here.

def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, cart_product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.cart_quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, cart_product=product, cart_quantity=1)

    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, cart_product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.cart_quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, cart_product=product, cart_quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    return render(request, 'carts/cart.html')


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])

