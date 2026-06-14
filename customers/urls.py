from django.urls import path
from . import views

urlpatterns = [
    # Dashboard page
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    # Customers list page (staff only)
    path(
        "customers/",
        views.customers_list,
        name="customers"
    ),

    # Profile page (ADDED FIX)
    path(
        "profile/",
        views.profile,
        name="profile"
    ),
]