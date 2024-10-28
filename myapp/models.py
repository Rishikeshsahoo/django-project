from django.db import models

#Company data
class Company(models.Model):
    company_name=models.CharField(max_length=100,null=False)
    number_of_employees=models.IntegerField(default=0)
    company_address=models.CharField(max_length=255)
    COMPANY_TYPE_CHOICES = [
        ('tech', 'Tech'),
        ('non-tech', 'Non-Tech'),
        ('financial', 'Financial'),
        ('healthcare', 'Healthcare'),
    ]

    company_type=models.CharField(max_length=10,choices=COMPANY_TYPE_CHOICES,default='tech')
    def __str__(self):
        return self.company_name
    
#Project data

class Project(models.Model):
    project_name=models.CharField(max_length=100,null=False)
    project_duration=models.IntegerField()
    start_date=models.DateField()
    status=models.CharField(max_length=50)
    number_of_member=models.IntegerField()
    
    def __str__(self):
        return self.project_name
    
    
    #employee data
class Employees(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_email=models.CharField(max_length=100)
    emp_phone_number=models.CharField(max_length=15)
    emp_address=models.Charfield(max_length=255)
    join_date=models.DateField()
    emp_salary = models.DecimalField(max_digits=10, decimal_places=2)
    emp_dob=models.CharField(max_length=12)
    is_manager=models.Boolean(default=True)
    
    #add forreign key for company and project id
    
    def __str__(self):
        return self.emp_name
    

    
    
    


