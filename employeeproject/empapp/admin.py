from django.contrib import admin
from empapp.models import Employee
from import_export.admin import ImportExportModelAdmin
#from empapp.models import views

#@admin.register(view)
class Employeeadmin(ImportExportModelAdmin):
    list_display=['employee_fullname','email_id','gender','Profile_Pic','employee_status']
    
admin.site.register(Employee,Employeeadmin)
