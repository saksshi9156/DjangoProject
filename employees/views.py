from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request, 'employees/index.html', {
        'employees': Employee.objects.all()
    })
    
    def view_employee(request, id):
        employee = Employee.objects.get(pk=id)
        return HttpResponseRedirect(reverse('index'))
    
    def add(request):
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                new_employee_number = form.cleaned_data['employee_number']
                new_first_name = form.cleaned_data['first_name']
                new_last_name = form.cleaned_data['last_name']
                new_email = form.cleaned_data['email']
                new_designation = form.cleaned_data['designation']
                new_salary = form.cleaned_data['salary']
        
        new_employee = Employee(
            employee_number = new_employee_number,
            first_name = new_first_name,
            last_name = new_last_name,
            email = new_email,
            designation = new_designation, 
            salary  = new_salary  
        )
        
        new_employee.save()
        return render(request, 'employee/add.html',{
            'form': EmployeeForm(),
            'success': True
        })
    else: 
        form = EmployeeForm()
        return render(request, 'employees/add.html',{
            'form':StudentForm()
        })
 
