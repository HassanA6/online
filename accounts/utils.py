from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, message
from django.conf import settings


def detectUser(user):
    if user.role == 1:
        redirectUrl = "restaurantDashboard"
        return redirectUrl
    elif user.role == 2:
        redirectUrl = "customerDashboard"
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = "/admin"
        return redirectUrl
        # comment:

def send_verification_email(request, user, mail_subject, email_template):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    print("current_site is " + current_site.domain)  # Access the domain attribute
    # print("current_site is " + current_site)  # Access current_site
    message = render_to_string(
        email_template,
        {
            "user": user,
            "domain": current_site.domain,  # Use current_site.domain
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user),
        },
    )
    print(message)
    to_email = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()

def send_vendor_email(mail_subject, mail_template, context):
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string(
        mail_template,
        context,
    )    
    to_email = context['user'].email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()








