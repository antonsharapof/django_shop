from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category as CategoryModel, Product as ProductModel, Order as CustomerOrder
from django.contrib.auth.models import User
from .serializer import CategorySerializer, ProductSerializer, OrderSerializer

class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class Category(viewsets.ViewSet):
    def list(self, request):
        cat = CategoryModel.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = ProductModel.objects.filter(category=pk)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

class Product(viewsets.ViewSet):

    def list(self, request):
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        product = ProductModel.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryProduct(viewsets.ViewSet):

    def retrieve(self, request, category):
        product = ProductModel.objects.filter(category=category)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class Cart(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request):
        user = User.objects.get_by_natural_key(request.user)
        orders = CustomerOrder.objects.filter(customer=user.id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

