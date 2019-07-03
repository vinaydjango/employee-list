from django import forms
from django.forms import ModelForm
from empapp.models import Employee

# Create the form class.
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
