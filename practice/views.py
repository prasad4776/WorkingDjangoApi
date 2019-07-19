from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employees,Departments
from . serializers import EmployeeSerializer,CombinedSerializer

from collections import namedtuple
from rest_framework.viewsets import ViewSet
Timeline = namedtuple('Timeline', ('a', 'b'))
# Create your views here.


    
    
class TimelineViewSet(APIView):
    """
    A simple ViewSet for listing the employees and departments in your Timeline.
    """
    def list(self, request):
        timeline = Timeline(
            a=Employees.objects.all(),
            b=Departments.objects.all(),
        )
        serializer = CombinedSerializer(timeline)
        return Response(serializer.data)