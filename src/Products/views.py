from django.shortcuts import render

from Products.models import Catalog, SubCatalog


def delete(request):
    SubCatalog.objects.all().delete()
    Catalog.objects.all().delete()
    return render(request, "delete.html")