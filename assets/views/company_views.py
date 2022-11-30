from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from assets.models import *
from assets.serializers.company_serializers import CompanySerializer
from assets.serializers.distribution_serializers import DistributionSerializer


# get all company data and create company
@api_view(['GET', 'POST'])
def companyGetPost(request):
    '''
    Retrun all company data.
    Create company data.
     '''

    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update or delete a company.
@api_view(['GET', 'PUT', 'DELETE'])
def companyGetUpdateDelete(request, pk):
    '''
    Retrun single company data.
    Update single company data.
    Delete single company data.
     '''

    try:
        company = Company.objects.get(pk=pk)
    except company.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def checkAssetReturn(request, pk):
    '''
    Each company should be able to see when a Device was checked out and returned
     '''

    employees = Employee.objects.filter(company__pk=pk).values('pk')
    print(employees)
    distributions = Distribution.objects.filter(employee__pk__in=[
        i['pk'] for i in employees
    ])
    print(distributions)
    serializer = DistributionSerializer(distributions, many=True)
    return Response(serializer.data)
