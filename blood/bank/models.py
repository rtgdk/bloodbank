from __future__ import unicode_literals
from django.db import models
import os
from datetime import datetime
from bank import cities
from django import forms
    
class Blood_Bank(models.Model):
	user_name = models.CharField(max_length=64)
	password = models.CharField(max_length=64)
	bank_name = models.CharField(max_length=64,blank=False)
	address = models.CharField(max_length=128)
	lat = models.FloatField(('Latitude'), blank=True, null=True)
	lon = models.FloatField(('Longitude'), blank=True, null=True)
	logo = models.URLField(max_length=256)
	city = models.CharField(choices=cities.city,max_length=64,blank=False)
	reg_no = models.IntegerField(blank=True,null=True)
	phone_no = models.IntegerField(blank=False,null=True)
	A_plus = models.IntegerField(blank=True,null=True, default=0)
	A_minus = models.IntegerField(blank=True,null=True, default=0)
	B_plus = models.IntegerField(blank=True,null=True, default=0)
	B_minus = models.IntegerField(blank=True,null=True, default=0)
	AB_plus = models.IntegerField(blank=True,null=True, default=0)
	AB_minus = models.IntegerField(blank=True,null=True, default=0)
	O_plus = models.IntegerField(blank=True,null=True, default=0)
	O_minus = models.IntegerField(blank=True,null=True, default=0)
	Ffp = models.IntegerField(blank=True,null=True, default=0)
	Plt = models.IntegerField(blank=True,null=True, default=0)
	Cry = models.IntegerField(blank=True,null=True, default=0)
	Lpl = models.IntegerField(blank=True,null=True, default=0)
	Aph = models.IntegerField(blank=True,null=True, default=0)
	Unt = models.IntegerField(blank=True,null=True, default=0)
	Ca_plus = models.IntegerField(blank=True,null=True, default=0)
	Ca_minus = models.IntegerField(blank=True,null=True, default=0)
	Cb_plus = models.IntegerField(blank=True,null=True, default=0)
	Cb_minus = models.IntegerField(blank=True,null=True, default=0)
	Cab_plus = models.IntegerField(blank=True,null=True, default=0)
	Cab_minus = models.IntegerField(blank=True,null=True, default=0)
	Co_plus = models.IntegerField(blank=True,null=True, default=0)
	Co_minus = models.IntegerField(blank=True,null=True, default=0)
	last_updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user_name
	@staticmethod
	def authenticate(username=None, pass_word=None):
		try:
		    user = Blood_Bank.objects.get(user_name = username)
		    if user.password == pass_word:
		        return 1
		    else:
		        return 0
		except Blood_Bank.DoesNotExist:
		    return 0

class Guest(models.Model):
	name = models.CharField(max_length=64)
	mobile_no = models.IntegerField(blank=False,null=True)
	def __str__(self):
		return self.name


