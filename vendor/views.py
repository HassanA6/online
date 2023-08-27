from multiprocessing import context
from unicodedata import category
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from accounts.forms import UserProfileForm
from accounts.models import Userprofile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
import vendor

from vendor.forms import VendorForm
from vendor.models import Vendor
from accounts.views import check_role_vendor
from menu.models import Category, FoodItem
from vendor.utils import get_vendor


# Create your views here.
@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def resProfile(request):
    profile = get_object_or_404(Userprofile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, "Your profile was successfully updated!")
            return redirect("resProfile")
        else:
            messages.error(request, "Please fill correctly.")
            print(profile_form.errors)
            print(vendor_form.errors)

    profile_form = UserProfileForm(instance=profile)
    vendor_form = VendorForm(instance=vendor)

    context = {
        "profile": profile,
        "vendor": vendor,
        "profile_form": profile_form,
        "vendor_form": vendor_form,
    }
    return render(request, "vendor/resProfile.html", context)

@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def menuBuilder(request):
    vendor = get_vendor(request)
    # categories = vendor.categories.all()
    categories = Category.objects.filter(vendor=vendor)

    context = {
        "vendor": vendor,
        "categories": categories,
    }
    return render(request, "vendor/menuBuilder.html", context)

@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def food_items_by_category(request, pk=None):
    vendor = get_vendor(request)
    category = get_object_or_404(Category, pk=pk)
    food_items = FoodItem.objects.filter(vendor=vendor, category=category)
    context = {
        "vendor": vendor,
        "category": category,
        "food_items": food_items,
    }
    return render(request, "vendor/foodItemsByCategory.html", context)
