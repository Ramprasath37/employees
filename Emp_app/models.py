from django.db import models

# Create your models here.

class EMPLOYEE(models.Model):


    ADMIN = "Admin"
    HR = "Hr"
    MARKETING = "Marketing"
    EXECUTIVE = "Executive"
    IT = "IT"
    ACCOUNTING = "Accounting"
    SALES = "Sales"

    Department_Choice =[
        (ADMIN , "Admin"),
        (HR, "Hr"),
        (MARKETING, "Marketing"),
        (EXECUTIVE , "Executive"),
        (IT , "IT"),
        (ACCOUNTING , "Accounting"),
        (SALES , "Sales")


    ]

    Emp_Name = models.CharField(max_length=30)
    Emp_Id = models.IntegerField()
    Emp_Email_Id = models.EmailField()
    Emp_Mobile_No = models.IntegerField()
    Emp_Address = models.CharField(max_length=40)
    Emp_Department = models.CharField(
        max_length=10,
        choices=Department_Choice,
        default= HR,
    )


