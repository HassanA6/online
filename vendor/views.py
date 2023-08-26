from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from accounts.forms import UserProfileForm
from accounts.models import Userprofile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

from vendor.forms import VendorForm
from vendor.models import Vendor
from accounts.views import check_role_vendor






# Create your views here.
@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def resProfile(request):
    profile = get_object_or_404(Userprofile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST,request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('resProfile')
        else:
            messages.error(request, 'Please fill correctly.')
            print(profile_form.errors)
            print(vendor_form.errors)

    profile_form = UserProfileForm(instance=profile)
    vendor_form = VendorForm(instance=vendor)

    context = {
        'profile': profile,
        'vendor': vendor,

        'profile_form': profile_form,
        'vendor_form': vendor_form,

    }
    return render(request, 'vendor/resProfile.html',context)