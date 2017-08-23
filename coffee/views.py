from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.http import Http404, JsonResponse
from decimal import Decimal
import json



def coffee_price(instance):
	total_price = instance.bean.price + instance.roast.price + (instance.shots*Decimal(0.250))
	if instance.milk:
		total_price+= Decimal(0.100)
	if instance.powders.all().count()>0:
		for powders in instance.powders.all():
			total_price+= powders.price
	if instance.syrups.all().count()>0:
		for syrups in instance.syrups.all():
			total_price+= syrups.price
	return total_price		

def usersignup(request):
	context = {}
	form = UserSignup()
	context['form'] = form
	if request.method == 'POST':
		form = UserSignup(request.POST)
		if form.is_valid():
			user = form.save()
			username = user.username
			password = user.password

			user.set_password(password)
			user.save()

			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)

			
		messages.error(request, form.errors)
		return redirect("coffee:signup")
	return render(request, 'signup.html', context)

def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form
	if request.method == 'POST':
		form = UserLogin(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('coffee:login')
				

			messages.error(request, "Wrong username/password combination. Please try again.")
			return redirect("coffee:login")
		messages.error(request, form.errors)
		return redirect("coffee:login")
	return render(request, 'login.html', context)

def userlogout(request):
	logout(request)
	return redirect("coffee:login")

def bean_list(request):
	object_list = Bean.objects.all()

	context = {
	"object_list": object_list
	}

	return render(request, 'bean_list.html', context)	

def bean_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = BeanForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")
		return redirect("coffee:beanlist")
	context = {
	"title": "Bean",
	"form": form,
	}
	return render(request, 'bean_create.html', context)

def bean_update(request, post_id):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Bean, id=post_id)
	form = BeanForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Updated!")
		return redirect("coffee:beanlist")
	context = {
	"title": "Bean",
	"form": form,
	'instance': instance,
	}
	return render(request, 'bean_update.html', context)

def bean_delete(request, post_id):
	instance = get_object_or_404(Bean, id=post_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("coffee:beanlist")

def powder_list(request):
	object_list = Powder.objects.all()

	context = {
	"object_list": object_list
	}

	return render(request, 'powder_list.html', context)		

def powder_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404	
	form = PowderForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")
		return redirect("coffee:powderlist")
	context = {
	"title": "Powder",
	"form": form,
	}
	return render(request, 'powder_create.html', context)

def powder_update(request, post_id):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Powder, id=post_id)
	form = PowderForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Updated!")
		return redirect("coffee:powderlist")
	context = {
	"title": "Powder",
	"form": form,
	'instance': instance,
	}
	return render(request, 'powder_update.html', context)

def powder_delete(request, post_id):
	instance = get_object_or_404(Powder, id=post_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("coffee:powderlist")

def roast_list(request):
	object_list = Roast.objects.all()

	context = {
	"object_list": object_list
	}

	return render(request, 'roast_list.html', context)				

def roast_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404	
	form = RoastForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")
		return redirect("coffee:roastlist")
	context = {
	"title": "Roast",
	"form": form,
	}
	return render(request, 'roast_create.html', context)

def roast_update(request, post_id):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Roast, id=post_id)
	form = RoastForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Updated!")
		return redirect("coffee:roastlist")
	context = {
	"title": "Roast",
	"form": form,
	'instance': instance,
	}
	return render(request, 'roast_update.html', context)

def roast_delete(request, post_id):
	instance = get_object_or_404(Roast, id=post_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("coffee:roastlist")

def syrup_list(request):
	object_list = Syrup.objects.all()

	context = {
	"object_list": object_list
	}

	return render(request, 'syrup_list.html', context)		

def syrup_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404	
	form = SyrupForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")
		return redirect("coffee:syruplist")
	context = {
	"title": "Syrup",
	"form": form,
	}
	return render(request, 'syrup_create.html', context)

def syrup_update(request, post_id):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Syrup, id=post_id)
	form = SyrupForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Updated!")
		return redirect("coffee:syruplist")
	context = {
	"title": "Syrup",
	"form": form,
	'instance': instance,
	}
	return render(request, 'syrup_update.html', context)

def syrup_delete(request, post_id):
	instance = get_object_or_404(Syrup, id=post_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("coffee:syruplist")

def coffee_list(request):
	object_list = Coffee.objects.filter(user=request.user)

	context = {
	"object_list": object_list
	}

	return render(request, 'coffee_list.html', context)	

def coffee_create(request):
	form = CoffeeForm(request.POST or None)
	if form.is_valid():
		coffee = form.save(commit=False)
		coffee.user = request.user
		coffee.save()
		form.save_m2m()
		coffee.price = coffee_price(coffee)
		coffee.save()
		messages.success(request, "Successfully Created!")
		return redirect("coffee:coffeelist")
	context = {
	"title": "Coffee",
	"form": form,
	}
	return render(request, 'coffee_create.html', context)

def coffee_update(request, post_id):
	instance = get_object_or_404(Coffee, id=post_id)
	form = CoffeeForm(request.POST or None, instance = instance)
	if form.is_valid():
		coffee = form.save(commit=False)
		coffee.user = request.user
		coffee.save()
		form.save_m2m()
		messages.success(request, "Successfully Updated!")
		return redirect("coffee:coffeelist")
	context = {
	"title": "Coffee",
	"form": form,
	'instance': instance,
	}
	return render(request, 'coffee_update.html', context)

def coffee_delete(request, post_id):
	instance = get_object_or_404(Coffee, id=post_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("coffee:coffeelist")

def coffee_detail(request, post_id):
	instance = get_object_or_404(Coffee, id=post_id)

	context = {
	"instance":instance,
	}

	return render(request, 'coffee_detail.html', context)

def adress_list(request):
	object_list = Adress.objects.all()

	context = {
	"object_list": object_list
	}

	return render(request, 'adress_list.html', context)		

def adress_create(request):
	form = AdressForm(request.POST or None)
	if form.is_valid():
		adress = form.save(commit=False)
		adress.user = request.user
		adress.save()
		messages.success(request, "Successfully Created!")
		return redirect("coffee:adresslist")
	context = {
	"title": "Adress",
	"form": form,
	}
	return render(request, 'adress_create.html', context)

def adress_update(request, post_id):
	instance = get_object_or_404(Adress, id=post_id)
	form = AdressForm(request.POST or None, instance = instance)
	if form.is_valid():
		adress = form.save(commit=False)
		adress.user = request.user
		adress.save()
		messages.success(request, "Successfully Updated!")
		return redirect("coffee:adresslist")
	context = {
	"title": "Adress",
	"form": form,
	'instance': instance
	}
	return render(request, 'adress_update.html', context)

def adress_delete(request, post_id):
	instance = get_object_or_404(Adress, id=post_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("coffee:adresslist")			

def coffee_pricecalc(request):
	
	total = Decimal(0)

	bean_id = request.GET.get('bean')
	if bean_id:
		total+= Bean.objects.get(id=bean_id).price

	roast_id = request.GET.get('roast')
	if roast_id:
		total+= Roast.objects.get(id=roast_id).price	

	shots = request.GET.get('shots')
	total += Decimal(int(shots) * 0.200)

	milk = request.GET.get('milk')
	if milk == 'true':
		total += Decimal(0.250)

	syrups = json.loads(request.GET.get('syrups'))
	for syrup in syrups:
		total += Syrup.objects.get(id=syrup).price

	powders = json.loads(request.GET.get('powders'))
	for powder in powders:
		total += Powder.objects.get(id=powder).price

	print (round(total, 3))
	return JsonResponse(round(total, 3), safe=False)





