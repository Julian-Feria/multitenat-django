from django.shortcuts import render
from productos.models import Productos

from productos.serializer import PoductosSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet




class ProductosViewSet(ModelViewSet):
    queryset = Productos.objects.all()  
    serializer_class = PoductosSerializer