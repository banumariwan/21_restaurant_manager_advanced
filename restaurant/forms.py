from django import forms
from .models import Table, MenuItem, Order



class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'



class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'