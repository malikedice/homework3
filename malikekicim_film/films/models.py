# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	city = models.CharField(max_length=60)
	country = models.CharField(max_length=50)
	publisher_fav = models.BooleanField(default=False)


	def __str__(self):
		return self.name


class Director(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	director_fav = models.BooleanField(default=False)

	def __str__(self):
		return self.first_name + " " + self.last_name

class Film(models.Model):
	title = models.CharField(max_length=100)
	publication_date = models.DateField()
	director = models.ManyToManyField(Director)
	publisher = models.ForeignKey(Publisher)
	film_fav = models.BooleanField(default=False)

        def __str__(self):
                return self.title
# Create your models here.
