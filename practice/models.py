from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length = 50)
    salary = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
class Departments(models.Model):
    dept_name = models.CharField(max_length = 50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name
    