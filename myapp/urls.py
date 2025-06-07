from django.urls import path
from django.contrib.auth.views import LoginView
from . import views  # Import views correctly

urlpatterns = [
    path('', views.first, name='home'),  # Ensure the 'first' view is defined in views.py
    path('login/',views.second,name='second'),
    path('home/',views.third,name='third'),
    path('ordes/',views.four,name='four'),
    path('ord/',views.five,name='five'),
    path('or/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_item_from_cart, name='remove_item_from_cart'),
    path('men/',views.men,name='men'),
    path('women/',views.women,name='women'),
    path('kids/',views.kids,name='kids'),
    path('About/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('help/',views.help,name='help'),
    path('message/',views.customer_msg,name='customer_msg'),



]
