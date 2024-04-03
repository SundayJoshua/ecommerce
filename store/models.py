from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __int__(self):
		return self.user


class Product(models.Model):
	name = models.CharField(max_length=200, default=False)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	digital = models.BooleanField(default=False, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	quantity =models.IntegerField(default=1, null=True, blank=True)
# sehemu ya picha

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


# total ya individual products na quantity

	@property
	def get_total(self):
		total = sum([self.price * self.quantity])
		return total
	


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, blank=True)
	transaction_id = models.CharField(max_length=200, null=True)
	
	

	def __str__(self):
		return str(self.id)
	
#sehemu ya kwanza
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

#sehemu ya shipping

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping  


class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
	
		


class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=False, default=False)
	city = models.CharField(max_length=200, null=False, default=False)
	state = models.CharField(max_length=200, null=False, default=False)
	zipcode = models.CharField(max_length=200, null=False, default=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address









	


