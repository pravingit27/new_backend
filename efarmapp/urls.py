from django.urls import path
from django.conf.urls import url
from .views import ListCategory,DetailCategory,ListUser,DetailUser,ListCart,DetailCart,ListProduct,DetailProduct
#from views import product_view

urlpatterns = [
    
    path('category',ListCategory.as_view(),name='categories'),
    path('category/<int:pk>/',DetailCategory.as_view(),name='singlecategory'),

    path('products',ListProduct.as_view(),name='products'),
    path('products/<str:pk>/',DetailProduct.as_view(),name='singleproduct'),
    #path('products/getbyUsername/',DetailProduct.as_view(),name='productview'),
    #url(r'^products/(?P<name>\w+)/$', product_view ,name='profile_view'),

    path('users',ListUser.as_view(),name='users'),
    path('users/<int:pk>/',DetailUser.as_view(),name='singleusers'),

    path('carts',ListCart.as_view(),name='carts'),
    path('carts/<int:pk>/',DetailCart.as_view(),name='singlecart'),
]
