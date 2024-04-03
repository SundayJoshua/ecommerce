def store(request):
	items = Item.objects.all()
	orders = Order.objects.all()
	cartItems = CartItem.objects.all()
	context = {'item':items, 'order':orders, 'cartItem':cartItems}
	return render(request, 'store/store.html', context)



	 path('store/', views.store, name='store'),