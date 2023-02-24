from django.db import models
from django.contrib.auth.models import User
from Seller.models import Product
import uuid


class Buyer(models.Model):
    buyer= models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    first_name=models.CharField(max_length=200,blank=True, null=True)
    last_name=models.CharField(max_length=200,blank=True, null=True)
    email=models.EmailField(max_length=500, blank=True, null=True)
    adress=models.CharField(max_length=200,blank=True, null=True)
    profile_image=models.ImageField(null=True,blank=True, 
                                    upload_to='profiles/', default='profiles/user-default.png')

    created=models.DateTimeField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    def __str__(self):
        return str(self.first_name)
    


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)
        
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total
    
    


    
