from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    console = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="products", null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promo = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Vous pouvez ajouter d'autres champs au panier, comme la date de création, le total, etc.

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Vous pouvez également inclure d'autres champs pour les attributs des produits, comme la taille, la couleur, etc.

    def total_price(self):
        return self.product.price * self.quantity
