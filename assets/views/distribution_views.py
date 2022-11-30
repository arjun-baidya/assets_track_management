from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from assets.models import *
from assets.serializers.distribution_serializers import DistributionSerializer


@api_view(['GET','POST'])
def distributionsGetPost(request):
    '''
    Retrun all distribution data.
    Create distribution data.
     '''

    if request.method == 'GET':
        distributions = Distribution.objects.all()
        serializer = DistributionSerializer(distributions, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DistributionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update or delete a distribution.
@api_view(['GET', 'PUT', 'DELETE'])
def distributionGetUpdateDelete(request,pk):
    '''
    Retrun single distribution data.
    Update single distribution data.
    Delete single distribution data.
     '''

    try:
        distribution = Distribution.objects.get(pk=pk)
    except distribution.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DistributionSerializer(distribution,many=False)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DistributionSerializer(distribution, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        distribution.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

