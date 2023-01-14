from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from .models import Brand
from .serializers import BrandSerializer
from rest_framework.decorators import api_view
# Create your views here.


def home(request):
    return HttpResponse('Django is on track')


@api_view(['GET', 'POST', 'PUT'])
def brand_list(request):
    if request.method == 'GET':
        obj = Brand.objects.all()
        print(request.body)
        print(request.data)
        serializer = BrandSerializer(obj, many=True)
        print(serializer.data)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('baddd')
            return Response(serializer.errors)


@api_view(['PUT', 'DELETE'])
def brand_update(request, pk):
    if request.method == 'PUT':
        obj = Brand.objects.get(id=pk)
        serializer = BrandSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print('bad request')
            return Response(serializer.errors)

    if request.method == 'DELETE':
        obj = Brand.objects.get(id=pk)
        obj.delete()
        return Response('deleted successfully')



