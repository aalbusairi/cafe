from django.shortcuts import render, redirect
from .models import Cart, CartItem, Order
from coffee.models import Coffee

def mycart(request):
	cart, created = Cart.objects.get_or_create(user = request.user)

	item_id = request.GET.get("item")
	qty = request.GET.get("qty", 1)

	if item_id:
		coffee = Coffee.objects.get(id=item_id)
		cart_item, created = CartItem.objects.get_or_create(cart=cart, item=coffee)

		if int(qty)<1:
			cart_item.delete()
		else:
			cart_item.quantity= int(qty)
			cart_item.save()

	return render(request, 'cart.html', {'cart': cart})

def checkout(request):
	cart, created = Cart.objects.get_or_create(user=request.user)
	order, created = Order.objects.get_or_create(cart=cart, user=request.user)

	if order.address == None:
		return redirect("coffee:adressselect")
	return redirect("/") #payment page			
	