from django.shortcuts import get_object_or_404, render
from menu.models import Category

from vendor.models import Vendor

# Create your views here.


def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
    vendor_counters = vendors.count()
    
    context = {
        'vendors': vendors,
        'vendor_counters': vendor_counters,
    }

    return render(request, "marketplace/list_res.html", context)


def vendor_details(request, vendor_slug):
    vendor = get_object_or_404(Vendor, vendor_slug=vendor_slug)


    categories = Category.objects.filter(vendor=vendor)




    context = {
        'vendor': vendor,
        'categories': categories,
    }

    return render(request, "marketplace/vendor_details.html", context)


