from django.contrib import admin
from Emp_app.models import EMPLOYEE


# Register your models here.

class Emp_admin(admin.ModelAdmin):
    Emp_list = ["Emp_Name", "Emp_Id", "Emp_Email_Id", "Emp_Mobile_No", "Emp_Address", "Emp_Department " ]
     

admin.site.register(EMPLOYEE,Emp_admin)
