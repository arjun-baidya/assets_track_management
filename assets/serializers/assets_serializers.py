from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
# import refresh token from simple jwt
from assets.models import *


# Assets serializer
class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ['_id','asset_name', 'asset_type', 'asset_condition']


