from . models import Employees,Departments
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employees
        fields = ('id','name','salary')
        
class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Departments
        fields = ('id','dept_name','city')
        
class CombinedSerializer(serializers.Serializer):
    a = EmployeeSerializer(many = True)
    b = DepartmentSerializer(many = True)
    