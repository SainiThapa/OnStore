from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from Products.models import Catalog, SubCatalog

# Create your views here.
def home(request):
    return render(request,"index.html")

def products(request):
    return render(request,"products/products.html")

def contactus(request):
    return render(request, "products/contactus.html")

def categories(request):
    return render(request,"products/categories.html")

def user_required(user):
    return user.is_authenticated

@user_passes_test(user_required)
def cart(request):
    return render(request, "products/mycart.html")

