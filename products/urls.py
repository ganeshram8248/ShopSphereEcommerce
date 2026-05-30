from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.products_page,
        name="products"
    ),

    path(
        "detail/<int:id>/",
        views.product_detail,
        name="product_detail"
    ),

]