from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .models import Shopdata
from .serializers import Serializedata
from rest_framework import status
from django.shortcuts import  get_object_or_404
# Create your views here.


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
  
    return Response(api_urls)



@api_view(['POST'])
def add_data(request):
    item = Serializedata(data = request.data)

    if Shopdata.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    print(item.is_valid())
    if item.is_valid():
        item.save()
        print('valid data')
        return Response(item.data)
    else:
        print('not valid data')
        return Response(status = status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_info(request):
    if request.query_params:
        items = Shopdata.objects.filter(**request.query_param.dict())
    else:
        items = Shopdata.objects.all()
    print(items)

    if items:
        data = Serializedata(items)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def update_items(request, pk):
    item = Shopdata.objects.get(pk=pk)
    data = Serializedata(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_data(request, pk):
    item = get_object_or_404(Shopdata, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)