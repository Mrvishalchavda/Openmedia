from django.urls import path 
from . import views 

urlpatterns = [ 
    path('',views.home,name = "home"),
    path("signup",views.register,name = "home"),
    path("home",views.home,name = "home"),
    path("login",views.loginuser,name="login"),
    path("register",views.register,name="register")
    ]