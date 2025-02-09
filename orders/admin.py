from django.contrib import admin

from orders.models import OrderItem, Order

# Register your models here.


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'name', 'price', 'quantity']
    search_fields = ['product', 'name']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'address_delivery', 'requires_delivery', 'payment_on_get', 'is_paid', 'status']
    inlines = (OrderItemTabulareAdmin,)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'name', 'price', 'quantity']
