from django.contrib import admin

from .models import *
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('_id','company_name', 'company_address', 'company_email')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('_id','employee_name', 'employee_designation', 'employee_email','company')

class AssetsAdmin(admin.ModelAdmin):
    list_display = ('_id','asset_name', 'asset_type', 'asset_condition')


class DistributionAdmin(admin.ModelAdmin):
    list_display = ('_id','employee','asset_name', 'issue_date','checkout_date','asset_return_condition')


admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Assets, AssetsAdmin)
admin.site.register(Distribution,DistributionAdmin)