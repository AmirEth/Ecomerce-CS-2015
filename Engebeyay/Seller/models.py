from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Seller(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    first_name=models.CharField(max_length=200,blank=True, null=True)
    last_name=models.CharField(max_length=200,blank=True, null=True)
    phone_number=models.IntegerField(max_length=455, blank=True, null=True)
    email=models.EmailField(max_length=500, blank=True, null=True)
    adress=models.CharField(max_length=200,blank=True, null=True)
    profile_image=models.ImageField(null=True,blank=True, 
                                    upload_to='profiles/', default='profiles/user-default.png')
    verification_image=models.ImageField(null=True,blank=True, 
                                    upload_to='profiles/')

    created=models.DateTimeField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    def __str__(self):
        return str(self.username)
    



class Product(models.Model):
    username= models.ForeignKey(Seller,on_delete=models.CASCADE, null=True, blank=True)
    product_name=models.CharField(max_length=200,blank=True, null=True)
    catagory=models.CharField(max_length=200,blank=True, null=True)
    stock= models.IntegerField(max_length=455, blank=True, null=True)
    
    decription=models.TextField(max_length=500, blank=True, null=True)
    Product_image=models.ImageField(null=True,blank=True, 
                                    upload_to='profiles/', default='profiles/user-default.png')

    created=models.DateTimeField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    def __str__(self):
        return str(self.product_name)
