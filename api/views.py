from django.shortcuts import HttpResponse
from rest_framework.response import Response
from .models import Brand
from .serializers import BrandSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.


def home(request):
    return HttpResponse('Django is on track')


class BrandList(GenericAPIView, ListModelMixin, CreateModelMixin):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        print(self.serializer_class)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            print('serializer', serializer)
            serializer.save()
            return self.create(request, *args, **kwargs)

        return Response(serializer.errors, status=status.HTTP_200_OK)



class BrandUpdate(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


