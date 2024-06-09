from django.contrib import admin
from django.urls import path
from Emp_app import views


urlpatterns = [
    # path("",views.home),
    # path("Emp_details/",views.view_Employees),
    path("",views.view_Employees),

    path("add_employee/",views.Add_Employee),
    path("edit_employee/ <int:id>",views.Edit_Employee),
    path("delete_employee/ <int:id>",views.Delete_Employee),

    
]
