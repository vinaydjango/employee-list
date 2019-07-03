from django.db import models
from django.urls import reverse
class Employee(models.Model):
    Gender_status=(('male','Male'),('Female','Female'))
    employee_status=(('enable','Enable'),('disable','Desable'))
    employee_fullname=models.CharField(max_length=100)
    email_id=models.EmailField()
    gender=models.CharField(max_length=10,choices=Gender_status,default='Male')
    Profile_Pic=models.ImageField(upload_to='images/')
    employee_status=models.CharField(max_length=10,choices=employee_status,default='Male')

def get_absolute_url(self):
    return reverse('detail',kwargs={'pk':self.pk})
