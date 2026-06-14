from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('add/<int:id>/', views.add_cart, name='add_cart'),
    path('remove/<int:id>/', views.remove_cart, name='remove_cart'),
    path('increase/<int:id>/', views.increase_qty, name='increase_qty'),
    path('decrease/<int:id>/', views.decrease_qty, name='decrease_qty'),
]