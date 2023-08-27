from django.contrib import admin

from menu.models import Category, FoodItem

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'vendor', 'created_at', 'updated_at')
    list_filter = ('category_name', 'vendor', 'created_at', 'updated_at')
    search_fields = ('category_name', 'vendor__vendor_name', 'created_at', 'updated_at')
    ordering = ['category_name']


class FoodItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('food_title',)}
    list_display = ('food_title', 'slug', 'vendor', 'category', 'price', 'is_available', 'created_at', 'updated_at')
    list_filter = ('food_title', 'vendor', 'category', 'price', 'is_available', 'created_at', 'updated_at')
    search_fields = ('food_title', 'vendor__vendor_name', 'category__category_name', 'price', 'is_available', 'created_at', 'updated_at')
    ordering = ['food_title']

admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodItem, FoodItemAdmin)