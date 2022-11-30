from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from assets.models import *
from assets.serializers.employee_serializers import EmployeeSerializer


# get all employee data and create employee
@api_view(['GET', 'POST'])
def getEmployees(request):
    '''
    Retrun all employee data.
    Create employee data.
     '''

    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update or delete a employee.
@api_view(['GET', 'PUT', 'DELETE'])
def getEmployee(request,pk):
    '''
    Retrun single employee data.
    Update single employee data.
    Delete single employee data.
     '''

    try:
        employee = Employee.objects.get(pk=pk)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee,many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




