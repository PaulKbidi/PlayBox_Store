# chat/urls.py
from django.urls import path
from. import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('cancel/', views.cancel, name='cancel'),
    path('success/', views.success, name='success'),
    path('checkout/', views.checkout, name='checkout'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('delete-item/<int:item_id>', views.delete_item, name='delete_item-url'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart-url'),
    path('contact/', views.contact, name='contact-url'),
    path('a-propos/', views.a_propos, name='a-propos-url'),
    path('panier/', views.panier, name='panier-url'),
    path('product/<int:pk>', views.product, name='product-url'),
    path('catalogue/', views.catalogue, name='catalogue-url'),
    path('', views.store, name='store-url'),
]
