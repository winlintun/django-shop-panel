from pyexpat import model
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        #fields = ['status', 'customer'] # select it
        fields = '__all__'