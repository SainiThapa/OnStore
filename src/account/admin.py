from django.contrib import admin

from account.models import Client, Merchant

# Register your models here.
admin.site.register(Client)
admin.site.register(Merchant)
