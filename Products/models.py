import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    category = models.ForeignKey(SubCatalog,verbose_name="Category",on_delete=models.CASCADE)
    product_name = models.CharField(max_length=128)
    product_img=models.ImageField()
    product_id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_price =  models.FloatField()
    product_rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    added_to_cart = models.BooleanField(default=False)
    def __str__(self) -> str:
        return (f"{self.product_name} - {self.product_id}")

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart_quantity=models.IntegerField()
    total_price=models.FloatField()
    def __str__(self) -> str:
        return f"{self.product} - {self.total_price}"