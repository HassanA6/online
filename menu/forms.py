from dataclasses import fields
from django import forms
from accounts.validators import allow_only_image_upload

from menu.models import Category, FoodItem

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']


class FoodItemForm(forms.ModelForm):
    # image = forms.FileField(
    #     widget=forms.FileInput(attrs={"class": "btn btn-info w-100"}),
    #     validators=[allow_only_image_upload],
    # )

    image = forms.FileField(
        widget=forms.FileInput(attrs={"class": "btn btn-info w-100"}),
        validators=[allow_only_image_upload]
    )

    
    class Meta:
        model = FoodItem
        fields = ['category', 'food_title', 'description', 'price', 'image', 'is_available']
        