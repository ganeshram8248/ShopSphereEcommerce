from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path(
        '',
        views.index,
        name='index'
    ),

    path(
        'inventory/',
        views.inventory,
        name='inventory'
    ),

    path('cart/', include('cart.urls')),

    path('products/', include('products.urls')),

    path(
        'product/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),
    path('customers/', include('customers.urls')),

    path(
        'buy/<int:id>/',
        views.buy_now,
        name='buy_now'
    ),
    path(
       'all/',
        views.all_orders,
        name='all_orders'
    ),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("logout/", views.logout_view, name="logout"),

    path("orders/", views.orders, name="orders"),
    path("all-orders/", views.all_orders, name="all_orders"),
    path("dashboard/", views.customer_dashboard, name="customer_dashboard"),
    
 #   path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("seller-dashboard/", views.seller_dashboard, name="seller_dashboard"),

    path(
        'vendor/',
        include('vendors.urls')
    ),
    path("checkout/<int:id>/", views.checkout, name="checkout"),
    path("order-success/", views.order_success, name="order_success"),
    path("admin/", admin.site.urls),
    path("profile/", views.profile, name="profile"),
    #path('profile/', include('userprofile.urls')),
    path("wishlist/", include("userwishlist.urls")),
    path('remove-wishlist/<int:id>/', views.remove_wishlist, name='remove_wishlist'),
    path("", include("userprofile.urls")),
    #path("profile/", include("userprofile.urls")),
    path('cancel-order/<int:id>/', views.cancel_order, name='cancel_order'),
    path('settings/', views.settings_view, name='settings'),
    # urls.py
    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
