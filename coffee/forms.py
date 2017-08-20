from django.contrib.auth.models import User
from django import forms
from .models import *

class UserSignup(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']

		widgets={
		'password': forms.PasswordInput(),
		}

class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class BeanForm(forms.ModelForm):
	class Meta:
		model = Bean
		fields = ['name', 'price', 'type']

class PowderForm(forms.ModelForm):
	class Meta:
		model = Powder
		fields = ['name', 'price']

class RoastForm(forms.ModelForm):
	class Meta:
		model = Roast
		fields = ['roast', 'price']

class SyrupForm(forms.ModelForm):
	class Meta:
		model = Syrup
		fields = ['name', 'price']

class CoffeeForm(forms.ModelForm):
	class Meta:
		model = Coffee
		fields = ['name','shots','bean','roast','syrups','powders','water','milk','foam','extrainstructions']						

