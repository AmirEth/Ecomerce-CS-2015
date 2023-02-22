from django.db import models
from django.contrib.auth.models import User
from Seller.models import Product
import uuid


class Buyer(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    first_name=models.CharField(max_length=200,blank=True, null=True)
    last_name=models.CharField(max_length=200,blank=True, null=True)
    email=models.EmailField(max_length=500, blank=True, null=True)
    adress=models.CharField(max_length=200,blank=True, null=True)
    profile_image=models.ImageField(null=True,blank=True, 
                                    upload_to='profiles/', default='profiles/user-default.png')

    created=models.DateTimeField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    def __str__(self):
        return str(self.username)
    


class Order(models.Model):
    buyer=models.OneToOneField(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    Product= models.OneToOneField(Product,on_delete=models.CASCADE, null=True, blank=True)
    product_name=models.CharField(max_length=200,blank=True, null=True)
    catagory=models.CharField(max_length=200,blank=True, null=True)
    stock= models.IntegerField(max_length=455, blank=True, null=True)
    
    decription=models.TextField(max_length=500, blank=True, null=True)
    Product_image=models.ImageField(null=True,blank=True, 
                                    upload_to='profiles/', default='profiles/user-default.png')

    created=models.DateTimeField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    def __str__(self):
        return str(self.username)
    


    