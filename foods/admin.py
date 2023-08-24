from django.contrib import admin
from .models import Category, User, Food, SubCategory


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'first_name', 'active']



@admin.register(SubCategory)
class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register((Category, Food))
