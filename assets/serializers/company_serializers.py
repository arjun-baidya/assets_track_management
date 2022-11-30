from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
# import refresh token from simple jwt
from assets.models import *


# Company serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['_id', 'company_name', 'company_address', 'company_email']
