from django.db import models
from accounts.models import User, Userprofile


# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    user_profile = models.OneToOneField(Userprofile, related_name="userprofile", on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=50)
    vendor_license = models.FileField(upload_to="vendor/license")
    # vendor_logo = models.ImageField(upload_to="vendor/logo")
    # vendor_address = models.TextField()
    # vendor_email = models.EmailField()
    # vendor_phone = models.CharField(max_length=50)
    # vendor_website = models.CharField(max_length=50)
    # vendor_category = models.CharField(max_length=50)
    # vendor_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)



    def __str__(self):
        return self.vendor_name