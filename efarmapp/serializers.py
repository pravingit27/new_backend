from rest_framework import serializers
from .models import Category,Product,cart
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
   
   class Meta:
       fields = (
           'id',
           'title'
       )
       model = Category

#class ProductUserSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = User
   #     fields = ('username')

    #def method(self, obj):
     #   return obj.username

class ProductSerializer(serializers.ModelSerializer):
    #created_by = ProductUserSerializer(read_only=True,many=False)
    #created_by = serializers.ReadOnlyField(source='created_by.username')
    #category = serializers.CharField(source ='category.title')

    class Meta:
        fields = (
            #'id',
            'name',
            #'slug',
            'category',
            'price',
            'quantity',
            'image',
            'created_by',
            'date_created'
        )
        model = Product

    def to_representation(self,instance):
        product = super(ProductSerializer,self).to_representation(instance)
        product['category'] = instance.category.title
        return product
               

class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    
    class Meta:
        model = User
        fields = (
             'id',
             'username',
             'email',
             'products',
        )

class CartUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','email')

class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True, many=False)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = cart
        fields = (
            'cart_id',
            'created_at',
            'products',
        )