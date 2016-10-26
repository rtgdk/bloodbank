from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from bank.forms import GuestForm, BloodBankLogin, GuestForm2 , BloodBankform
from bank.models import Blood_Bank, Guest
import json
Logged_In=0
name=''
def index(request) :
	global Logged_In
	if request.method == 'POST':
		form = GuestForm(data=request.POST)
		form2 = GuestForm2(data=request.POST)
		if form.is_valid() and form2.is_valid():
			count=form.save(commit=False)
			if len(str(count.mobile_no))==10:
				count.save()
				count2=form2.save(commit=False)
				a=count2.city
				b='/bank/city/'
				c=b+a
				return HttpResponseRedirect(c)
			else :
				return HttpResponse("Not a valid mobile no.")
		else :
			print form.errors
	else:	
		form= GuestForm()
		form2 = GuestForm2()

	return render(request,'bank/index.html',{'form': form,'form2': form2})

def login(request):
	global Logged_In,name
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = Blood_Bank.authenticate(username,password)
		if user==1 :
			Logged_In=1
			name=username
			return HttpResponseRedirect('/bank/')
		else :
			return HttpResponseRedirect('/bank/not_registered')
	else:	
		return render(request,'bank/login.html')
def not_registered(request):
	return render(request,'bank/not_registered.html')



def logout(request):
	global Logged_In
	Logged_In=0
	return HttpResponseRedirect('/bank/')

def blood_count(request):
	global Logged_In,name
	if Logged_In == 1 and request.method == 'POST':
		a = Blood_Bank.objects.get(user_name=name)
		form = BloodBankform(request.POST,instance = a)
		if form.is_valid() :
			count=form.save(commit=False)
			count.last_updated=datetime.now()
			count.save()
		else :
			print form.errors
	elif Logged_In == 0 :
		return HttpResponse("Log in to view and update blood counts")	

	else:
		a = Blood_Bank.objects.get(user_name=name)
		form = BloodBankform(instance=a)
	return render(request,'bank/blood_count.html',{'form': form})

def search(request):
	if request.method == 'POST':
		form = GuestForm(data=request.POST)
		form2 = GuestForm2(data=request.POST)
		if form.is_valid() and form2.is_valid():
			count=form.save(commit=False)
			count.save()
			count2=form2.save(commit=False)
			a=count2.city
			b='/bank/city/'
			c=b+a
			return HttpResponseRedirect(c)
			
		else :
			print form.errors
	else:	
		form= GuestForm()
		form2 = GuestForm2()
	return render(request,'bank/search.html',{'form': form,'form2': form2})


def city(request,place):
	try:
		banks = Blood_Bank.objects.filter(city = place)
		context_dict = {'banks': banks,'city':place}
	except Blood_Bank.objects.filter(city = place).DoesNotExist:
		pass
	return render(request,'bank/city.html', context=context_dict)




def navigate(request,user):
	banks = Blood_Bank.objects.get(user_name = user)
	lat = json.dumps(banks.lat)
	lon = json.dumps(banks.lon)
	context_dict = {'banks': banks,'user':user,'lat':lat,'lon':lon}
	return render(request,'bank/navigate.html', context=context_dict)
