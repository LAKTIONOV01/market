from django.urls import path
from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('profile/', user_profile, name='profile'),
    path('user-cart/', user_cart, name='user-cart'),
    path('logout/', user_logout, name='logout'),
]
