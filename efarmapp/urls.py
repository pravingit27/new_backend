from django.urls import path,include
from django.conf.urls import url
from .views import ListCategory,DetailCategory,ListCart,DetailCart,ListProduct,DetailProduct,ListAdmin
from . import views
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'admin', views.ListAdmin)
router.register(r'admin/<str:pk>',views.ListAdmin)

urlpatterns = [
    
    path('category',ListCategory.as_view(),name='categories'),
    path('category/<int:pk>/',DetailCategory.as_view(),name='singlecategory'),

    path('products',ListProduct.as_view(),name='products'),
    path('products/<str:pk>',DetailProduct.as_view(),name='singleproduct'),
    #path('products/getbyUsername/',DetailProduct.as_view(),name='productview'),
    #url(r'^products/(?P<name>\w+)/$', product_view ,name='profile_view'),

    #path('seller',ListAdmin.as_view(),name='admin'),
    path('login',views.signin,name='login'),
    path('logout/<str:username>/',views.signout,name='logout'),

    #path('users',ListUser.as_view(),name='users'),
    #path('users/<int:pk>/',DetailUser.as_view(),name='singleusers'),

    path('carts',ListCart.as_view(),name='carts'),
    path('carts/<int:pk>/',DetailCart.as_view(),name='singlecart'),
    path('',include(router.urls))
]
