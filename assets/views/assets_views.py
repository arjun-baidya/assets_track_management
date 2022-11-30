from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from assets.models import *
from assets.serializers.assets_serializers import AssetsSerializer


@api_view(['GET', 'POST'])
def assetsGetPost(request):
    '''
    Retrun all asset data.
    Create asset data.
     '''

    if request.method == 'GET':
        assets = Assets.objects.all()
        serializer = AssetsSerializer(assets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AssetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def assetGetUpdateDelete(request,pk):
    '''
    Retrun single asset data.
    Update single asset data.
    Delete single asset data.
     '''

    try:
        asset = Assets.objects.get(pk=pk)
    except asset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AssetsSerializer(asset)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AssetsSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    