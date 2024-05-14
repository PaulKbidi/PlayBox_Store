# chat/urls.py
from django.urls import path
from. import views

urlpatterns = [
    path('panier/', views.panier, name='panier-url'),
    path('product/<int:pk>', views.product, name='product-url'),
    path('catalogue/', views.catalogue, name='catalogue-url'),
    path('', views.store, name='store-url'),
]
