from rest_framework import serializers
from .models import Company
# create serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"