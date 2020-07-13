from django.db import models

# Create your models here.

## Inheriting from djangodb models classes

## CharField goes with max_length which is required
## https://docs.djangoproject.com/en/3.0/ref/models/fields/
## There can be a default argument in a TextField


# Product.objects.create(title="Product 2", price='30', summary='Awesome product')

class Product(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField(blank=True, null=True)
    price           = models.DecimalField(decimal_places=2, max_digits=100)
    summary         = models.TextField()
    featured        = models.BooleanField(null=True)
# featured = models.BooleanField(null=True) or default=True
# If were to do this : would NULL all the previous values
# If want to set a value for all the previous products :
# Previous values for each product
