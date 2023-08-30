from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from accounts.forms import UserProfileForm
from accounts.models import Userprofile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from menu.forms import FoodItemForm, categoryForm

from vendor.forms import VendorForm
from vendor.models import Vendor
from accounts.views import check_role_vendor
from menu.models import Category, FoodItem
from vendor.utils import get_vendor
from django.template.defaultfilters import slugify

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
    categories = Category.objects.filter(vendor=vendor).order_by('created_at')

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



@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def addCategory(request):
    if request.method == "POST":
        form = categoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data["category_name"]
            category = form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, "Category added successfully")
            return redirect("menuBuilder")
        else:
            messages.error(request, "Please fill correctly.")
            print(form.errors)
    else:

        form = categoryForm()
    context = {
        "form": form,
    }
    return render(request, "vendor/addCategory.html", context)

@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def editCategory(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = categoryForm(request.POST, instance=category)
        if form.is_valid():
            category_name = form.cleaned_data["category_name"]
            category = form.save(commit=False)
            category.vendor = get_vendor(request)
            category.slug = slugify(category_name)
            form.save()
            messages.success(request, "Category Updated successfully")
            return redirect("menuBuilder")
        else:
            messages.error(request, "Please fill correctly.")
            print(form.errors)
    else:
        form = categoryForm(instance=category)
    context = {
        "form": form,
        'category': category,
    }
    return render(request, "vendor/editCategory.html", context)


@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def deleteCategory(request, pk=None):
    category = get_object_or_404(Category, pk=pk)
    # delete the category
    category.delete()
    messages.success(request, "Category deleted successfully")
    return redirect("menuBuilder")



@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def addFoodItem(request, pk=None):
    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            food_title = form.cleaned_data["food_title"]
            food = form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(food_title)
            form.save()
            messages.success(request, "food added successfully")
            return redirect("foodItemsByCategory",food.category.id )
        else:
            messages.error(request, "Please fill correctly.")
            print(form.errors)
    else:
        form = FoodItemForm()
        form.fields['category'].queryset = Category.objects.filter(vendor=get_vendor(request))

    context = {
        "form": form,
    }

    return render(request, "vendor/addFoodItem.html", context)



@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def editFoodItem(request, pk=None):
    food = get_object_or_404(FoodItem, pk=pk)
    print("My food is : " + str(food))
    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES, instance=food)
        print("My form is : " + str(form))
        if form.is_valid():
            food_title = form.cleaned_data["food_title"]
            food = form.save(commit=False)
            food.vendor = get_vendor(request)
            food.slug = slugify(food_title)
            print("My food is edited: " + str(food))
            form.save()
            messages.success(request, "food Updated successfully")
            return redirect("foodItemsByCategory", food.category.id )
        else:
            messages.error(request, "Please fill correctly.")
            print(form.errors)
    else:
        form = FoodItemForm(instance=food)
        form.fields['category'].queryset = Category.objects.filter(vendor=get_vendor(request))

    context = {
        "form": form,
        'food': food,
    }
    return render(request, "vendor/editFood.html", context)


@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def deleteFoodItem(request, pk=None):
    food = get_object_or_404(FoodItem, pk=pk)
    # delete the category
    food.delete()
    messages.success(request, "Food deleted successfully")
    return redirect("foodItemsByCategory", food.category.id)
