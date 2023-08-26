import profile
from django import forms
from .models import User, Userprofile
from .validators import allow_only_image_upload


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput())
    # use the to show the errors in the same ones

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "confirmPassword",
            # "phone_number",
        ]

    def clean_confirmPassword(self):
        cleaned_data = super(UserForm, self).clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirmPassword")
        username1 = cleaned_data.get("username")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match what are you typing!")
        # check if username1 is already exits rase error

 
    labels = {
        "confirmPassword": "Confirm Password",
        "password:": "رمز عبور",
    }

    help_texts = {
        "username": None,
    }

    error_messages = {
        "username": {
            "This writer's name is too long.",
        },
    }


class UserProfileForm(forms.ModelForm):
    address = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    profile_pic = forms.FileField(
        widget=forms.FileInput(attrs={"class": "btn btn-info"}),
        validators=[allow_only_image_upload],
    )
    cover_pic = forms.FileField(
        widget=forms.FileInput(attrs={"class": "btn btn-info"}),
        validators=[allow_only_image_upload],
    )

    # latitude = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    # longitude = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = Userprofile
        fields = [
            "profile_pic",
            "cover_pic",
            "address",
            "country",
            "state",
            "city",
            "pin_code",
            "latitude",
            "longitude",
        ]

    def __init__(self, *args, **kwargs_):
        super(UserProfileForm, self).__init__(*args, **kwargs_)
        for field in self.fields:
            if field == "latitude" or field == "longitude":
                self.fields[field].widget.attrs["readonly"] = "readonly"
