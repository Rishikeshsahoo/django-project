from rest_framework import serializers
from .models import Employees, Project, Company

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'
