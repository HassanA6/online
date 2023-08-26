from django import forms

from accounts.validators import allow_only_image_upload, allow_pdf_image

from .models import Vendor


class VendorForm(forms.ModelForm):
    vendor_license = forms.FileField(
        widget=forms.FileInput(attrs={"class": "btn btn-info"}),
        validators=[allow_pdf_image],
    )


    class Meta:
        model = Vendor
        fields = [
            "vendor_name",
            "vendor_license",
        ]
