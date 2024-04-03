from django.urls import path
from django.contrib import admin
from . import views
from store import urls


urlpatterns = [
	path('', include('store.urls')),
]