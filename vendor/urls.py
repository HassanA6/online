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
    # category crud
    path("menu-builder/category/add/", views.addCategory, name="addCategory"),
    path('menu-builder/category/edit/<int:pk>/', views.editCategory, name='editCategory'),
    path('menu-builder/category/delete/<int:pk>/', views.deleteCategory, name='deleteCategory'),
    # # food item crud
    path("menu-builder/food-item/add/", views.addFoodItem, name="addFoodItem"),
    path('menu-builder/food-item/edit/<int:pk>/', views.editFoodItem, name='editFoodItem'),
    path('menu-builder/food-item/delete/<int:pk>/', views.deleteFoodItem, name='deleteFoodItem'),
    # # order crud
    # path("orders/", views.orders, name="orders"),
    # path("orders/<int:pk>/", views.orderDetails, name="orderDetails"),
    # path("orders/<int:pk>/update/", views.updateOrder, name="updateOrder"),
    # path("orders/<int:pk>/delete/", views.deleteOrder, name="deleteOrder"),
    # # reports
    # path("reports/", views.reports, name="reports"),
    # path("reports/<int:pk>/", views.reportDetails, name="reportDetails"),
    # path("reports/<int:pk>/delete/", views.deleteReport, name="deleteReport"),
    # # reviews
    # path("reviews/", views.reviews, name="reviews"),
    # path("reviews/<int:pk>/", views.reviewDetails, name="reviewDetails"),
    # path("reviews/<int:pk>/delete/", views.deleteReview, name="deleteReview"),
    # # notifications
    # path("notifications/", views.notifications, name="notifications"),
    # path("notifications/<int:pk>/", views.notificationDetails, name="notificationDetails"),
    # path("notifications/<int:pk>/delete/", views.deleteNotification, name="deleteNotification"),
    # # settings
    # path("settings/", views.settings, name="settings"),
    # path("settings/<int:pk>/", views.settingDetails, name="settingDetails"),
    # path("settings/<int:pk>/delete/", views.deleteSetting, name="deleteSetting"),
    # # payments
    # path("payments/", views.payments, name="payments"),
    # path("payments/<int:pk>/", views.paymentDetails, name="paymentDetails"),
    # path("payments/<int:pk>/delete/", views.deletePayment, name="deletePayment"),
    # # coupons
    # path("coupons/", views.coupons, name="coupons"),
    # path("coupons/<int:pk>/", views.couponDetails, name="couponDetails"),
    # path("coupons/<int:pk>/delete/", views.deleteCoupon, name="deleteCoupon"),
    # # coupons
    # path("promotions/", views.promotions, name="promotions"),
    # path("promotions/<int:pk>/", views.promotionDetails, name="promotionDetails"),
    # path("promotions/<int:pk>/delete/", views.deletePromotion, name="deletePromotion"),
    # # coupons
    # path("referrals/", views.referrals, name="referrals"),

]
