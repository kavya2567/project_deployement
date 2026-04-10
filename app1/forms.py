from django import forms
from app1.models import employee   
class employee_form(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'

class employee_delete(forms.Form):
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=10)
    
