# chat/urls.py
from django.urls import path
from. import views

urlpatterns = [
    path('contact/', views.contact, name='contact-url'),
    path('a-propos/', views.a_propos, name='a-propos-url'),
    path('panier/', views.panier, name='panier-url'),
    path('product/<int:pk>', views.product, name='product-url'),
    path('catalogue/', views.catalogue, name='catalogue-url'),
    path('', views.store, name='store-url'),
]
