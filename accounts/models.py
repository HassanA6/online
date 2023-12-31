from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have an email address")

        # what dose user do?
        # explain

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True

        user.is_active = True
        user.is_staff = True

        user.is_superadmin = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    RESTAURANT = 1
    CUSTOMER = 2

    ROLE_CHOICES = (
        (RESTAURANT, "Restaurant"),
        (CUSTOMER, "Customer"),
    )

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    username = models.CharField(max_length=50, unique=True)

    email = models.EmailField(
        # verbose_name='email address',
        max_length=255,
        unique=True,
    )

    phone_number = models.CharField(max_length=50, blank=True)

    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default=CUSTOMER, blank=True, null=True
    )

    # required FIeldS

    date_joined = models.DateTimeField(auto_now_add=True)

    last_login = models.DateTimeField(auto_now_add=True)

    created_data = models.DateTimeField(auto_now_add=True)

    modified_data = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)

    is_superadmin = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""

        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""

        # Simplest possible answer: Yes, always
        return True

    def get_role(self):
        if self.role == 1:
            return "Restaurant"
        elif self.role == 2:
            return "Customer"


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    profile_pic = models.ImageField(
        blank=True, upload_to="users/profile_pics", null=True
    )

    cover_pic = models.ImageField(blank=True, upload_to="users/cover_pics", null=True)

    address = models.TextField(blank=True, null=True, max_length=255)

    country = models.CharField(max_length=20, blank=True, null=True)

    state = models.CharField(max_length=20, blank=True, null=True)

    city = models.CharField(max_length=20, blank=True, null=True)

    pin_code = models.CharField(max_length=10, blank=True, null=True)

    latitude = models.CharField(max_length=20, blank=True, null=True)

    longitude = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    # def fullAddress(self):
    #     return f"{self.address_line_1} {self.address_line_2}"