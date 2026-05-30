from django.urls import path
from userprofile import views

urlpatterns = [

    path('profile/', views.profile, name='profile'),
    path("login/",views.login_page,name="login"),
    path("register/",views.register_page,name="register"),
    path("logout/", views.logout_page,name="logout"),

]