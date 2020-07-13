from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    print(request.user)
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, "home.html", {})
    # {} is for "context"

def contact_view(request, *args, **kwargs):
    my_context = {
        'my_title' : 'You can contact us',
        'my_number' : '0608122766',
        'my_address' : '7, Rue Livingstone',
        'my_list' : [123, 456, 321, 789],
        'my_hmtl' : '<h1> This is a test HTML </h1>'
    }
    return render(request, "contact.html", my_context)

def about_view(*args, **kwargs):
    return HttpResponse('<h1>About Page</h1>')
