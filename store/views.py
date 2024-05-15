from django.shortcuts import render
from .models import Product
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .forms import ContactForm
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
        form = ContactForm()
    
    return render(request, 'store/contact.html', {'form': form})