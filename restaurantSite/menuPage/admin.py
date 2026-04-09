from django.contrib import admin
from .models import Person, Restaurant, FoodItem, MenuPageAdministration

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email']

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'food_type', 'food_description', 'food_price', 'food_thumbnail']

@admin.register(MenuPageAdministration)
class MenuPageAdministrationAdmin(admin.ModelAdmin):
    list_display = ['id', 'color']

admin.site.register(Restaurant)