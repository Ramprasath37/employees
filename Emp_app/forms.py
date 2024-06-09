from django import forms
from Emp_app.models import EMPLOYEE

class Emp_Form (forms.ModelForm):
    class Meta:

        model = EMPLOYEE
        fields = "__all__"

        widgets = {
            "Emp_Name" : forms.TextInput(attrs={"class":"form-control"}),
            "Emp_Id":forms.NumberInput(attrs={"class":"form-control"}),
            "Emp_Email_Id" : forms.EmailInput(attrs={"class":"form-control"}),
            "Emp_Mobile_No":forms.NumberInput(attrs={"class":"form-control"}),
            "Emp_Address":forms.TextInput(attrs={"class":"form-control"}),
            # "Emp_Department":forms.(attrs={"class":"form=control"})

        }

  