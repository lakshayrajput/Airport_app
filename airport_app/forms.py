from django import forms
from models import CustomerModel

class MobileForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ["mob_no"]






