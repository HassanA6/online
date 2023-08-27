from django.urls import include, path
from vendor import views
from accounts import views as AccountsViews


urlpatterns = [
    path("", AccountsViews.restaurantDashboard, name="restaurantDashboard"),
    path("profile/", views.resProfile, name="resProfile"),
    path("menu-builder/", views.menuBuilder, name="menuBuilder"),
    path(
        "menu-builder/category/<int:pk>/",
        views.food_items_by_category,
        name="foodItemsByCategory",
    ),
]
