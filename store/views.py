from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import json
import datetime
from .models import *
from . utils import cookieCart, cartData, guestOrder



def store(request):
	data = cartData(request)
	cartItems = data['cartItems']

	products = Product.objects.all()	
	context = {'products': products, 'cartItems': cartItems}


	#context['result'] = Product.objects.aggregate(total=Sum(F('price') * F('quantity')))
	#context['count'] = Product.objects.filter().aggregate(Sum('quantity'))
	return render(request, 'store/store.html', context)



def cart(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']  

	context = {'items': items, 'order': order, 'cartItems': cartItems}		
	return render(request, 'store/cart.html', context)



def checkout(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items': items, 'order': order, 'cartItems': cartItems}
	return render(request, 'store/checkout.html', context)



def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('action:', action)
	print('productId:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)



#from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)


	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == float(order.get_cart_total):
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
			customer=customer,
			order=order,
			name=data['shipping']['name'],
			email=data['shipping']['email'],
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment complete..', safe=False)


def search_view(request):
	if request.method == "POST":
		data = cartData(request)
		cartItems = data['cartItems']
		searched = request.POST['searched']
		products = Product.objects.filter(name__contains=searched)
		return render(request, "store/search.html", {"searched": searched, "products": products, "data": data, "cartItems": cartItems})

	else:
		return render(request, "store/search.html", {})
  

def foo(request):
	js_data = json.dumps(data)
	return JsonResponse('Processing....', {"data": js_data}, safe=False)

