from multiprocessing import context
from django.db import models
from accounts.models import User, Userprofile
from accounts.utils import send_vendor_email

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
    
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            old = Vendor.objects.get(pk=self.pk)
            if old.is_approved != self.is_approved:
                email_template = 'accounts/emails/account_vendor_email_approved.html'
                context = {
                        'is_approved': self.is_approved,
                        'Restaurant': self.vendor_name,
                        'first_name':self.user.first_name,
                        'user': self.user,
                        'email': self.user.email,
                        
                    }
                if self.is_approved ==True :
                    # send email to vendor
                    mail_subject = "Your account has been approved"
                    send_vendor_email(mail_subject, email_template,context=context)
                else:
                    # send email to vendor
                    mail_subject = "Your account has been rejected" 
                    send_vendor_email(mail_subject, email_template,context=context)

        return super(Vendor, self).save(*args, **kwargs)
        