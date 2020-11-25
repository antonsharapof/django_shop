from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        if self.discount:
            discount_price = self.price - self.price/100*self.discount
            return discount_price
        return self.price

class Gallery(models.Model):
    alt = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='gallery')

    def __str__(self):
        return self.alt