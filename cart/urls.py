from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^mycart/$', views.mycart, name="mycart"),
	url(r'^checkout/$', views.checkout, name="checkout"),
]