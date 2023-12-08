from django.urls import path
# from .views import ProductDetailView,ProductListlView
from .views import (manufacturer_list,manufacturer_detail,product_list,product_detail)

urlpatterns=[
#     path("",ProductListlView.as_view(),name='product-list'),
#     path('product/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),
      path('products/',product_list,name='product-list'),
      path('products/<int:pk>',product_detail,name='product-details'),
      path('manufacturers/',manufacturer_list,name='manufacturer-list'),
      path('manufacturers/<int:pk>',manufacturer_detail,name='manufacturers-details'),
 ]