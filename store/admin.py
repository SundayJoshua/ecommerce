from django.contrib import admin
from .models import *

from django.contrib.admin import ModelAdmin, SimpleListFilter


class Filter(admin.ModelAdmin):
	list_display = ("id", "name", "email", "customer", "address", "city", "state", "zipcode", "date_added")



admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress, Filter)


