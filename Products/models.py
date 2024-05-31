import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import Client

# Create your models here.
    
class Catalog(models.Model):
    catalog_name= models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.catalog_name}"

class SubCatalog(models.Model):
    catalog = models.ForeignKey(Catalog,verbose_name="Catalog",on_delete=models.CASCADE)
    subcatalog_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.catalog} - {self.subcatalog_name}"

class Product(models.Model):
    category = models.ForeignKey(SubCatalog,verbose_name="SubCatalog",on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    img=models.ImageField()
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    price =  models.FloatField()
    rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    added_to_cart = models.BooleanField(default=False)
    def __str__(self) -> str:
        return (f"{self.name} - {self.id}")

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    customer=models.OneToOneField(Client,on_delete=models.CASCADE,primary_key=True)

    def __str__(self) -> str:
        return f"Cart {self.id} created at {self.created_at}"

    def total_price(self):
        return sum(item.total_price() for item in self.cartitem_set.all())

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product} - {self.total_price}"
    
    def total_price(self):
        return self.quantity*self.product.price