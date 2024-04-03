from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("", views.store, name="store"),
    path("checkout/", views.checkout, name="checkout"),	
  	path("update_item/", views.updateItem, name="update_item"),
  	path('cart/', views.cart, name='cart'),
	path("process_order/", views.processOrder, name="process_order"),
    path("search/", views.search_view, name="search"),
]
