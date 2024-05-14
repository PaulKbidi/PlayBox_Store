from django.shortcuts import render
from .models import Product
# Create your views here.
def store(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products':products})

def catalogue(request):
    products = Product.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(title__icontains=search_query)

    console_filter = request.GET.get('console')
    if console_filter:
        products = products.filter(console=console_filter)

    price_range_filter = request.GET.get('price')
    if price_range_filter:
        min_price, max_price = price_range_filter.split('-')
        products = products.filter(price__gte=min_price, price__lte=max_price)

    context = {'filtered_products': products}
    return render(request, 'store/catalogue.html', context)

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product.html', {'product':product})

def panier(request):
    return render(request, 'store/panier.html')

def a_propos(request):
    return render(request, 'store/a_propos.html')

def contact(request):
    return render(request, 'store/contact.html')