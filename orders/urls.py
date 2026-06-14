from django.urls import path
from . import views

urlpatterns = [

    path('', views.orders_list, name='orders_list'),

    path('buy/<int:id>/', views.buy_now, name='buy_now'),

    path('cancel/<int:id>/', views.cancel_order, name='cancel_order'),

    path('all/', views.all_orders, name='all_orders'),
]