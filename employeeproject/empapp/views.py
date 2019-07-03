from django.shortcuts import render,HttpResponse
from empapp.forms import EmployeeForm
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from empapp.models import Employee
from django.shortcuts import redirect
class Employee_create(CreateView):
    model = Employee
    fields = ('employee_fullname','email_id','gender','Profile_Pic','employee_status')
    success_url="/"

class Employee_list_view(ListView):
    model = Employee


class Employee_details_view(DetailView):
    model = Employee

class Employee_update_view(UpdateView):
    model = Employee
    fields=('employee_fullname','email_id','gender','Profile_Pic','employee_status')
    success_url="/"

def Employee_delete_view(request,id):
    emp =Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')
import csv
def csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    employees = Employee.objects.all()
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.employee_fullname,employee.email_id,employee.gender])
    return response
