
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.



def dynamic_lookup_view(request, product_id):
    # Original version
    # obj = Product.objects.get(id=product_id)

    # 404 handling
    # obj = get_object_or_404(Product, id=product_id)

    # Or handling with try except method:
    try:
        obj = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404

    context = {
        'object' : obj
    }
    return render(request, "products/product_detail.html", context)

#############################################
# CREATE
#############################################

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # To reset and show a clear version of the form after saving
    context = {
                'form':form
              }
    return render(request, 'products/product_create.html', context)

#############################################
# LIST
#############################################

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render(request, 'products/product_list.html', context)

#############################################
# PRODUCT DETAILS
#############################################

def product_detail_view(request, id):
    #obj = Product.objects.get(id=2)
    obj = get_object_of_404(Product, id=id)
    ## Below : Not good because not dynamically picking up the new structure of the model - sort of hardcoded
    # context = {
    #     'title' : obj.title,
    #     'description' : obj.description
    # }
    context = {'object':obj}
    return render(request, "products/product_detail.html", context)
    # Failing
    #return render(request, "products/detail.html", context)

#############################################
# PRODUCT DELETION
#############################################

def product_delete_view(request, product_id):
    obj=get_object_or_404(Product, id = product_id)
    # here by default would happen with GET request
    # Want to do deletion with POST request : so create a FORM for it
    if request.method == 'POST':
        # Confirming if they want to delete
        obj.delete()
        return redirect('../../')
    context = {
        "object":obj
    }
    return render(request, "products/product_delete.html", context)


## New format - to render initial data

def render_initial_data(request):
    initial_data = {
        'title' : 'Initial title'
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form" : my_form
#     }
#     return render(request, "products/product_create.html", context)


# Old view : when doing raw HTML

# def product_create_view(request):
#     #print(request.GET)
#     #print(request.GET['title'])
#     #print(request.POST)
#     if request.method == "POST": # To not send None initially (only render when POST)
#         title = request.POST.get('title')
#         print(title)
#     context = {}
#     return render(request, "products/product_create.html", context)

# This is the old view // With Djando form data
