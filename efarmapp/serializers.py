from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
   
   class Meta:
       fields = (
           'id',
           'title'
       )
       model = Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'category',
            'price',
            'quantity',
            'image',
            'date_created'
        )
        model = Product

