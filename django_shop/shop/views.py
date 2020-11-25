from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category as CategoryModel, Product as ProductModel
from .serializer import CategorySerializer, ProductSerializer


class Category(viewsets.ViewSet):
    def list(self, request):
        cat = CategoryModel.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)

class Product(viewsets.ViewSet):

    def list(self, request):
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
