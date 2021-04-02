from django.shortcuts import render
from rest_framework import generics
from .models import Category,Product,cart
from django.contrib.auth.models import User
from .serializers import CategorySerializer,ProductSerializer,UserSerializer,CartSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['get'], detail=False,
            url_path='products/(?P<name>\w+)')
    def getByUsername(self, request, name):
        product = get_object_or_404(Product, name=name)
        data = ProductSerializer(product).data
        return Response(data, status=status.HTTP_200_OK)

    #lookup_field = 'slug'

class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCart(generics.ListCreateAPIView):
    queryset = cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    queryset = cart.objects.all()
    serializer_class = CartSerializer

    

    