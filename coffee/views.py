from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django.http import Http404

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


def bean_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	form = BeanForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")
	context = {
	"title": "Bean",
	"form": form,
	}
	return render(request, 'bean_create.html', context)

def bean_update(request, post_id):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404
	instance = get_object_or_404(Post, id=post_id)
	form = BeanForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")
	context = {
	"title": "Bean",
	"form": form,
	}
	return render(request, 'bean_update.html', context)	

def powder_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404	
	form = PowderForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")	
	context = {
	"title": "Powder",
	"form": form,
	}
	return render(request, 'powder_create.html', context)

def roast_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404	
	form = RoastForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")	
	context = {
	"title": "Roast",
	"form": form,
	}
	return render(request, 'roast_create.html', context)

def syrup_create(request):
	if not (request.user.is_staff or request.user.is_superuser):
		raise Http404	
	form = SyrupForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Successfully Created!")	
	context = {
	"title": "Syrup",
	"form": form,
	}
	return render(request, 'syrup_create.html', context)

def coffee_create(request):
	form = CoffeeForm(request.POST or None)
	if form.is_valid():
		user = request.user
		form.save()
		messages.success(request, "Successfully Created!")	
	context = {
	"title": "Coffee",
	"form": form,
	}
	return render(request, 'coffee_create.html', context)	


				






