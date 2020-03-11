from django.shortcuts import render
from .models import Product, Category,Brand
from django.http import JsonResponse

# Create your views here.
def product_details_view(request):
    context = None
    return render(request, "Product/details.html",context=context)



def data(request):

     context = {
        'product' : list(Product.objects.values()),
        'brand' : list(Brand.objects.values()),
        'category' : list(Category.objects.values())

     }
     return  JsonResponse(context,safe=False)