from django.contrib import admin

from Products.models import Catalog, Product, Cart, SubCatalog

# Register your models here.

admin.site.register(Product)    
admin.site.register(Cart)
admin.site.register(Catalog)
admin.site.register(SubCatalog)

