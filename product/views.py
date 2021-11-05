from django.shortcuts import render
from product.models import Product


# Create your views here.
def product(request):

    context ={
        'products':Product.objects.all()
    }

    return render(request,'product/display_product.html',context)


