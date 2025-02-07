from carts.models import Cart
from django import template

register = template.Library()


@register.simple_tag()
def user_carts(request):
    return Cart.objects.filter(user=request.user)
