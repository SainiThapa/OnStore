from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
User=get_user_model()

class Client(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone=models.IntegerField()
    address=models.CharField(max_length=128)
    interactions=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.user.username} - {self.user.id}"

class Merchant(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Company_name=models.CharField(max_length=128)
    phone=models.BigIntegerField()
    location=models.CharField(max_length=128)
    ratings = models.DecimalField(max_digits=2, decimal_places=1, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user.username} - {self.user.id} - {self.Company_name}"