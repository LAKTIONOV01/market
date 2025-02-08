from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from django.forms import ValidationError


# Create your views here.
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    cart_items = Cart.objects.filter(user=request.user)
                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=request.user,
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            address_delivery=form.cleaned_data['address_delivery'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        for cart_item in cart_items:
                            product = cart_item.cart_product
                            name = cart_item.cart_product.name
                            price = cart_item.cart_product.sell_price()
                            quantity = cart_item.cart_quantity

                            if product.quantity < quantity:
                                raise ValidationError(
                                    f'Недостаточно количество товара {name} на складе | В наличии {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                name=name,
                                price=price,
                                quantity=quantity
                            )
                            product.quantity - quantity
                            product.save()
                        cart_items.delete()
                        messages.success(request, 'Заказ оформлен')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.warning(request, str(e))
                return redirect('user:profile')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'form': form
    }
    return render(request, "orders/create_order.html", context)
