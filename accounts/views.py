from base64 import urlsafe_b64decode
import email
from email import message
import re
from click import confirm
from django.http import HttpResponse
from django.shortcuts import render
from accounts.utils import detectUser, send_verification_email
from django.contrib.auth.decorators import login_required, user_passes_test
from vendor.forms import VendorForm
from .models import User, Userprofile
from accounts.forms import UserForm
from django.contrib import messages, auth
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.template.defaultfilters import slugify



def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied


def register(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("MyAccount")

    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # passwords = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(passwords)
            # user.role = User.CUSTOMER
            # user.save()

            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.role = User.CUSTOMER
            user.save()

            mail_subject = "Please active your account"
            email_template = "accounts/emails/account_verification_email.html"
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, "Your account created successfully")

            return redirect("register")
        else:
            print(form.errors)
            print("user cant created at this moment 12-=")

    else:
        print("user cant created at this moment1-=")
        form = UserForm()

    context = {
        "form": form,
    }
    # return HttpResponse("accounts/registerUser.html")
    return render(request, "accounts/registerUser.html", context)


def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("MyAccount")
    elif request.method == "POST":
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.role = User.RESTAURANT
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            vendor_name = v_form.cleaned_data["vendor_name"]
            vendor.vendor_slug = slugify(vendor_name)+'-'+str(user.id)
            user_profile = Userprofile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            
            mail_subject = "please active your account"
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, "Your account created successfully")
            

            return redirect("registerVendor")
        else:
            print(form.errors)

    else:
        form = UserForm()
        v_form = VendorForm()

    context = {
        "form": form,
        "v_form": v_form,
    }
    return render(request, "accounts/registerVendor.html", context)


def activate(request, uidb64, token):
    print("activate for now")
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)  
        print("Gain information's right now")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        print("Exception:", e)
        user = None
        print("User not found")



    if user is not None and default_token_generator.check_token(user, token):
        print("Token generated successfully and will be used activated")
        user.is_active = True
        user.save()
        messages.success(request,"Your account is now active")
        return redirect("MyAccount")

    else:
        print("Please check email")
        messages.error(request,"Invalid link")
        return redirect("MyAccount")
    



def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        print("You are already logged in")
        return redirect("MyAccount")
    # check if user is already logged in
    elif request.method == "POST":
        email = request.POST.get("email")
        if email is not None:
            print("You are email in the database", email)
        else:
            print("email value is None or not found in POST data")        
        
        password = request.POST.get("password")
        if password is not None:
            print("You are Password in the database", password)
        else:
            print("Password value is None or not found in POST data")
            
            
        user = auth.authenticate(email=email, password=password)
                
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("MyAccount")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    return render(request, "accounts/login.html")


def logout(request):
    auth.logout(request)
    messages.info(request, "You are now logged out")
    return redirect("login")


@login_required(login_url="login")
def MyAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)


@login_required(login_url="login")
@user_passes_test(check_role_customer)
def customerDashboard(request):
    return render(request, "accounts/customerDashboard.html")


@login_required(login_url="login")
@user_passes_test(check_role_vendor)
def restaurantDashboard(request):
    return render(request, "accounts/restaurantDashboard.html")



@login_required(login_url="login")
def adminDashboard(request):
    return render(request, "accounts/adminDashboard.html")


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            
            mail_subject = "Rest Password"
            email_template = 'accounts/emails/rest_password_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'password link sent')
            return redirect('login')
        else:
            message.error(request, 'Account dose not exist')
            return redirect('forgot_password')
    return render(request, "accounts/forgot_password.html")
    
    
def rest_password_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)  
        print("Gain information's right now")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        print("Exception:", e)
        user = None
        print("User not found")  
        
        
        
    if user is not None and default_token_generator.check_token(user, token):
        request.session["uid"] = uid
        messages.info(request, "rest your password")
        return redirect("rest_password")
        
    else:
        messages.info(request, "This link is expired")
        return redirect("MyAccount")
        
               
def rest_password(request):
    if request.method == "POST":
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']
        
        if confirmPassword == password:
            
            pk = request.session.get("uid")
            user = User.objects.get(pk=pk)
            user.is_active = True
            user.set_password(password)
            user.save()
            messages.success(request,"Password changes successfully ")
            return redirect("login")
            
        else:
            messages.error(request, "The password dose not match")
            return redirect("rest_password")
    
    
    return render(request, "accounts/rest_password.html")