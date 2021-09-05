from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializers

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return Response('Hello')

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getProductId(request, pk):    
    pro = Product.objects.get(_id=pk)
    serializer = ProductSerializers(pro, many=False)
    return Response(serializer.data)