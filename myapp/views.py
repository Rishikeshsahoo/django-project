from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser
# Create your views here.
from .models import *
from .serializer import *

class EmployeeViewsets(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class CompanyViewsets(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]

