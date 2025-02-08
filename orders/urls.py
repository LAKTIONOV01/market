from django.urls import path
from orders.views import create_order

app_name = 'orders'

urlpatterns = [
   path('create-order/', create_order, name='add_order'),
]