from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
# import refresh token from simple jwt
from assets.models import *
from assets.serializers.company_serializers import CompanySerializer


# Employee serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [ '_id', 'employee_name', 'employee_designation','employee_email','company','company_name']


