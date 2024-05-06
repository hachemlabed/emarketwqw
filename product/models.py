from django.db import models
from account.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 255,default='')
    product = models.CharField(max_length = 255,default='')
    quantity = models.IntegerField(default = 0)
    description = models.CharField(max_length = 1000 , default="" )
    date_of_fabrication = models.DateField()
    date_of_expiration = models.DateField()
    image = models.ImageField(blank=True, null=True,upload_to='C:/Users/SBG/OneDrive/Documents/Bureau/APPMOBILEstore/product/images')
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    user = models.ForeignKey(User, null=True ,on_delete=models.CASCADE)