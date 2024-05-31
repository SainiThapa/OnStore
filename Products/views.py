from django.shortcuts import render

from Products.models import Catalog, SubCatalog

# Create your views here.
def home(request):
    return (request,"index.html")