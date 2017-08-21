from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Bean(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=6, decimal_places=3)
	type = models.CharField(max_length=15)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("coffee:beanupdate", kwargs={"post_id": self.id})

class Powder(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.name

class Roast(models.Model):
	roast = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.roast

class Syrup(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=6, decimal_places=3)

	def __str__(self):
		return self.name

class Coffee(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=20)
	shots = models.PositiveIntegerField(default=1)
	bean = models.ForeignKey(Bean, default=1)
	roast = models.ForeignKey(Roast, default=1)
	syrups = models.ManyToManyField(Syrup, blank=True)
	powders = models.ManyToManyField(Powder, blank=True)
	water = models.FloatField()
	milk = models.BooleanField(default=False)
	foam = models.FloatField()
	extrainstructions = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("coffee:coffeedetail", kwargs={"post_id": self.id})

class City(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Adress(models.Model):
	user = models.ForeignKey(User, default = 1)
	name = models.CharField(max_length=20, default=1)
	city = models.ForeignKey(City, default = 1)
	block = models.CharField(max_length=20)
	street = models.CharField(max_length=20)
	building = models.CharField(max_length=20, blank=True)
	floor = models.CharField(max_length=20, blank=True)
	apt_number = models.CharField(max_length=20, blank=True)
	extra_directions = models.TextField(null = True, blank=True)

	def __str__(self):
		return self.name






