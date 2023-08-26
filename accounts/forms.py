from django import forms
from .models import User


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
        if  password1 != password2:
            raise forms.ValidationError("Passwords do not match what are you typing!")
        # check if username1 is already exits rase error



    widgets = {
            "password": forms.PasswordInput(),
            "confirmPassword": forms.PasswordInput(),
        }
    labels = {"confirmPassword": "Confirm Password","password:": "رمز عبور",}
    
    help_texts = {
            "username": None,
        }
    
    error_messages = {
            "username": {
                "This writer's name is too long.",
            },
        }
