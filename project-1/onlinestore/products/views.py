from .models import Product,Manufacturer

from django.http import JsonResponse

def product_list(request):
    products=Product.objects.all()
    print(products)
    data={"products":list(products.values())}
    response=JsonResponse(data)
    return response

def product_detail(request,pk):
    try:
        product=Product.objects.get(pk=pk)
        data={
            "product":{
                "name":product.name,
                "manufacturer":product.Manufacturer.name,
                'description':product.description,
                'photo':product.photo.url,
                "price":product.price,
                'shipping_cost':product.shipping_cost,
                'quantity':product.quantity,
            }
        }
        response=JsonResponse(data)
        
    except Product.DoesNotExist:
        response=JsonResponse({
            "error":{
                "code":404,
                "message":"Product Not Found "
            }
        },status=404)
        
    return response

def manufacturer_list(request):
    manufacturer=Manufacturer.objects.filter(active=True)
    print(manufacturer)
    data={"products":list(manufacturer.values())}
    response=JsonResponse(data)
    return response

def manufacturer_detail(request,pk):
    try:
        manufacturer=Manufacturer.objects.get(pk=pk)
        manufacturer_products=manufacturer.products.all()
        data={
            "product":{
                "name":manufacturer.name,
                "manufacturer":manufacturer.location,
                'description':manufacturer.active,
                "products":list(manufacturer_products.values())
            }
        }
        response=JsonResponse(data)
        
    except Manufacturer.DoesNotExist:
        response=JsonResponse({
            "error":{
                "code":404,
                "message":"manufacturer Not Found "
            }
        },status=404)
        
    return response



# # from django.shortcuts import render
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView


# # Create your views here.

# class ProductDetailView(DetailView):
#     model=Product
#     template_name="products/product_detail.html"
    
# class ProductListlView(ListView):
#     model=Product
#     template_name="products/product_list.html"