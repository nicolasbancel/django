from django.db import models
from django.urls import reverse

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
    featured        = models.BooleanField(default=True,null=True)
# featured = models.BooleanField(null=True) or default=True
# If were to do this : would NULL all the previous values
# If want to set a value for all the previous products :
# Previous values for each product


# When we want to refer to the URL of a product ID, we can just store it here
# So don't have to hard code it again
# need the f string
    def get_absolute_url(self):
        #return f'/products/{self.id}/'
        # For reverse : use the friendly name given by
        return reverse('products:product-detail', kwargs={'id':self.id})
