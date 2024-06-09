from django.shortcuts import render,redirect
from django.http import HttpResponse 
from Emp_app.models import EMPLOYEE
from Emp_app.forms import Emp_Form

# Create your views here.

def home(request):
    # return HttpResponse("<h1>hiii</h1>")
    return render(request,"index.html")


def view_Employees(request):
    employee = EMPLOYEE.objects.all()

    return render(request,"Emp_Details.html",{"Employee_Details" :employee})



def Add_Employee(request):
    forms = Emp_Form()

    if request.method == "POST":
        form = Emp_Form(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("/Emp_details/") 
            return redirect("/") 

    return render(request,"add_employee.html",{"Form":forms})




def Edit_Employee(request,id):
    employee =EMPLOYEE.objects.get(id=id)
    context={
        "Employee" :Emp_Form(instance=employee)
    }

    if request.method == "POST":
        form = Emp_Form(request.POST,instance=employee)
        if form.is_valid:
            form.save()
            # return redirect("/Emp_details/")
            return redirect("/") 
 

    return render(request,"edit_employee.html",context)


def Delete_Employee(request,id):
    employee = EMPLOYEE.objects.get(id=id)
    employee.delete()
    # return redirect("/Emp_details/")
    return redirect("/") 





