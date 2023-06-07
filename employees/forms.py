from django import forms 
from .models import Employee

class EmployeeForm(forms.ModelForm):
    model = Employee
    fields = ['employee_number', 'first_name', 'last_name', 'email', 'designation', 'salary']
    labels = {
        'employee_number' :'Employee Number',
        'first_name' : 'First Name',
        'last_name' :'Last Name',
        'email' : 'Email',
        'designation' : 'Designation',
        'salary' : 'Salary'
    }
    widgets = {
        'employee_number' : forms.NumberInput(attrs={'class': 'form-control'}),
        'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
        'last_name' :forms.TextInput(attrs={'class': 'form-control'}),
        'email' : forms.EmailInput(attrs={'class': 'form-control'}),
        'designation' : forms.TextInput(attrs={'class': 'form-control'}),
        'salary' : forms.NumberInput(attrs={'class': 'form-control'}),
    }
    