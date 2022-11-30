from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
# import refresh token from simple jwt
from assets.models import *


# Distribution serializer
class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = ['_id','employee','employee_name','asset','asset_name', 'issue_date','checkout_date','asset_return_condition']




