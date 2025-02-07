from django.urls import path
from main.views import index, about

app_name = 'main'

urlpatterns = [
   path('', index, name='home'),
   path('about-us/', about, name='about')
]