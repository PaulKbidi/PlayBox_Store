from django.shortcuts import render
from .models import Product
# Create your views here.
def store(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products':products})

def catalogue(request):
    products = Product.objects.all()
    return render(request, 'store/catalogue.html', {'products':products})

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product.html', {'product':product})

def panier(request):
    return render(request, 'store/panier.html')