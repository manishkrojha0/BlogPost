from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer


# Create your views here.

class employeelist(APIView):

    def get(self, request):
        employees = employee.objects.all()
        serializer = employeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self):
        pass
