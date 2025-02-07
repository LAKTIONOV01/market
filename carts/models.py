from django.db import models

from goods.models import Product
from users.models import User


# Create your models here.

class QuerySetCart(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        return sum(cart.cart_quantity for cart in self)

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Клиент')
    cart_product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукт')
    cart_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество продукта')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    objects = QuerySetCart.as_manager()

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def products_price(self):
        return round(self.cart_product.sell_price() * self.cart_quantity, 2)

    def __str__(self):
        return f'Корзина: {self.user.username} | Товар {self.cart_product.name} | Количество {self.cart_quantity}'
