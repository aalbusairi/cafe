from django.db import models
from django.contrib.auth.models import User

class Bean(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	type = models.CharField(max_length=15)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("coffee:beanupdate", kwargs={"post_id": self.id})

class Powder(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name

class Roast(models.Model):
	roast = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.roast

class Syrup(models.Model):
	name = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name

class Coffee(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=20)
	shots = models.IntegerField()
	bean = models.ForeignKey(Bean, default=1)
	roast = models.ForeignKey(Roast, default=1)
	syrups = models.ManyToManyField(Syrup)
	powders = models.ManyToManyField(Powder)
	water = models.FloatField()
	milk = models.BooleanField()
	foam = models.FloatField()
	extrainstructions = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name





