from django.db import models
import string
# Create your models here.


# company model
class Company(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Company Name")
    company_address = models.CharField(max_length=200, verbose_name="Address")
    company_email = models.CharField(max_length=200, verbose_name="e-Mail")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.company_name

# Employee model
class Employee(models.Model):
    employee_name = models.CharField(max_length=100, verbose_name="Name")
    employee_designation = models.CharField(max_length=200, verbose_name="Designation")
    employee_email = models.CharField(max_length=200, verbose_name="e-Mail")
    company = models.ForeignKey(Company,related_name="company", on_delete=models.CASCADE, verbose_name="Company")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.employee_name
    @property
    def company_name(self):
        return self.company.company_name


# Assets model
asset_choise =(
    ("new", "NEW"),
    ("used", "USED"),
)

class Assets(models.Model):
    asset_name = models.CharField(max_length=100, verbose_name="Asset Name")
    asset_type = models.CharField(max_length=200, verbose_name="Asset Type")
    asset_condition = models.CharField(choices=asset_choise, max_length=50, null=True, verbose_name="Asset Condition")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.asset_name


# Distribution model
asset_condition =(
    ("ok", "Ok"),
    ("damaged", "Damaged"),
)
class Distribution(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Employee", related_name="employee_dist")
    asset = models.ManyToManyField(Assets, verbose_name="Asset")
    issue_date = models.DateTimeField( blank=True, verbose_name="Issue Date")
    checkout_date = models.DateTimeField(verbose_name="checkout Date")
    asset_return_condition = models.CharField(max_length=100,choices=asset_condition,null=True,blank=True,verbose_name="Asset Return Condition")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.employee)

    @property
    def employee_name(self):
        return self.employee.company_name
    
    @property
    def asset_name(self):
        return self.asset.values_list("asset_name")

    