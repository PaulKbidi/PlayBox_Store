from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    console = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="products", null= True)
    price = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    promo = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} - {self.picture}"