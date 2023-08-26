from django.urls import path
from accounts import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("registerVendor", views.registerVendor, name="registerVendor"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
]
