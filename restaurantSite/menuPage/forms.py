from django import forms
from .models import Restaurant, FoodItem

class RestaurantForm(forms.ModelForm):
    menu_items = forms.ModelMultipleChoiceField(
        queryset=FoodItem.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'phone_number', 'website', 'food_items']#, 'tables']

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'food_type', 'food_description', 'food_price', 'food_thumbnail']