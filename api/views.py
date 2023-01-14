from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from .models import Brand
from .serializers import BrandSerializer
from rest_framework.decorators import api_view
from rest_framework import  status
# Create your views here.


def home(request):
    return HttpResponse('Django is on track')


@api_view(['GET', 'POST'])
def brand_list(request):

    if request.method == 'GET':
        obj = Brand.objects.all()
        print('request.body', request.body)
        print('request.data', request.data)
        print('query_params', request.query_params)
        serializer = BrandSerializer(obj, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        print('request.body', request.body)
        print('request.data', request.data)
        print('query_params', request.query_params)
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'DELETE'])
def brand_update(request, pk):

    if request.method == 'PUT':
        obj = Brand.objects.get(id=pk)
        serializer = BrandSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        obj = Brand.objects.get(id=pk)
        serializer = BrandSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        obj = Brand.objects.get(id=pk)
        obj.delete()
        return Response(status.HTTP_200, status=status.HTTP_400_BAD_REQUEST)



