from django.shortcuts import render

from Products.models import Catalog, SubCatalog

# Create your views here.

def delete(request):
    SubCatalog.objects.all().delete()
    SubCatalog.save()
    Catalog.objects.all().delete()
    Catalog.save()
    return render(request, "delete.html")