from django.urls import include, path
from accounts import views

urlpatterns = [
    path('', views.MyAccount),
    path("register", views.register, name="register"),
    path("registerVendor", views.registerVendor, name="registerVendor"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("MyAccount", views.MyAccount, name="MyAccount"),
    path("adminDashboard", views.adminDashboard, name="adminDashboard"),
    path("customerDashboard", views.customerDashboard, name="customerDashboard"),
    path("restaurantDashboard", views.restaurantDashboard, name="restaurantDashboard"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),

    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('rest_password_validate/<uidb64>/<token>', views.rest_password_validate, name="rest_password_validate"),
    path('rest_password/', views.rest_password, name="rest_password"),

    path('restaurant/', include('vendor.urls')),
]
