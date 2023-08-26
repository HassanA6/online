from django.contrib import admin
from vendor.models import Vendor

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'vendor_license', 'created_at', 'modified_at', 'is_approved')
    list_display_links = ('vendor_name', 'vendor_license','user', 'modified_at' )
    list_editable = ('is_approved',)


admin.site.register(Vendor, VendorAdmin)


