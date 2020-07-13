
####################################################
# Get info from products
####################################################

# In terminal
# python manage.py shell

from products.models import Product

Product.objects.all()
obj = Product.objects.get(id=1)

# Commands to extract info from the obj
dir(obj)


# Product.objects.create(title='Product 2', description = 'Hello', price='78', summary='cool')
# Product.objects.create(title="Product 2", price='30', summary='Awesome product')

############################################################
## Tuto 11
############################################################

python manage.py startapp pages
