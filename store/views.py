from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Product, Cart, CartItem
from .forms import ContactForm, AddToCartForm
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import stripe
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def store(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})

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
    try:
        product = Product.objects.get(id=pk)
    except ObjectDoesNotExist:
        return redirect('store')

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            return redirect('panier')
    else:
        form = AddToCartForm()
    return render(request, 'store/product.html', {'product': product, 'form': form})

@login_required(login_url=reverse_lazy("login"))
def panier(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.quantity * item.product.price for item in items)
    return render(request, 'store/panier.html', {'items':items, 'total_price': total_price})

def a_propos(request):
    return render(request, 'store/a_propos.html')

def contact(request):
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    email_address = 'zeshortcut.contact@gmail.com'
    email_password = 'aale fcqb bvtp wmhx'

    email_receiver = 'paulkb57@gmail.com'

    context = ssl.create_default_context()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            firstname = form.cleaned_data["firstname"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            datas = f"Nom: {name}\nPrenom: {firstname}\nEmail: {email}\nMessage: {message}"

            msg = MIMEMultipart()
            msg['From'] = email_address
            msg['To'] = email_receiver
            msg['Subject'] = 'Nouveau message de contact'

            msg.attach(MIMEText(datas, 'plain'))

            with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
                server.login(email_address, email_password)
                server.send_message(msg)

            return render(request, 'store/contact.html')
    else:
        return render(request, 'store/contact.html')

@login_required(login_url=reverse_lazy("login"))
def add_to_cart(request, product_id):
    if request.method != 'POST':
        return redirect('store-url')

    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        return redirect('store-url')

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('catalogue-url')

@login_required(login_url=reverse_lazy("login"))
def delete_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('panier-url')

@login_required(login_url=reverse_lazy("login"))
def create_checkout_session(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user = request.user)
        items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.quantity * item.product.price for item in items)

        stripe.api_key = 'sk_test_51PGfwuP7Riw006UHWRQA5le0PlUx969sVprnJeT5TPS4Ldfhykv8nfsBBTrW16SwTbn4RQLgBVXcUPUCofOMjl2k00rimcF8Qc'
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': items,
                    },
                    'unit_amount': int(total_price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://paulkbidi.fr:5050/success',
            cancel_url='http://paulkbidi.fr:5050/cancel',
        )
        request.session['session_url'] = session.url
        return redirect('checkout')
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

@login_required(login_url=reverse_lazy("login"))
def checkout(request):
    session_url = request.session.get('session_url')
    return redirect(session_url)

def success(request):
    cart = Cart.objects.get(user = request.user)
    items = CartItem.objects.filter(cart=cart)
    items.delete()
    return render (request, 'store/success.html')

def cancel(request):
    return render(request, 'store/cancel.html')

def register(request):
	if request.method == 'POST' :
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()		
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request,user)	
			messages.success(request, f'Bonjour {username}, Votre compte a été créé avec succès !')					
			return redirect('store-url')
	else :
		form = UserCreationForm()
	return render(request,'store/register.html',{'form' : form})