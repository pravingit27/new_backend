from django.urls import path
from .views import ListCategory,DetailCategory,ListProduct,DetailProduct
urlpatterns = [
    path('category',ListCategory.as_view(),name='categories'),
    path('category/<int:pk>/',DetailCategory.as_view(),name='singlecategory'),

    path('products',ListProduct.as_view(),name='products'),
    path('products/<int:pk>/',DetailProduct.as_view(),name='singleproduct'),
]
