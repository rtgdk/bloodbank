from django import forms
from bank.models import Guest,Blood_Bank
from bank import cities
class BloodBankform(forms.ModelForm):
	class Meta:
		model = Blood_Bank
		fields = ('A_plus','A_minus','B_plus','B_minus', 'AB_plus','AB_minus','O_plus','O_minus','Ffp','Plt','Cry','Lpl','Aph','Unt','Ca_plus','Ca_minus', 
'Cb_plus','Cb_minus','Cab_plus','Cab_minus','Co_plus','Co_minus')
class GuestForm(forms.ModelForm):
	class Meta:
		model = Guest
		fields = ('name','mobile_no')

class BloodBankLogin(forms.ModelForm):
	class Meta:
		model = Blood_Bank
		fields = ('user_name','password')

class GuestForm2(forms.ModelForm):
	last_updated = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
	class Meta:
		model = Blood_Bank
		fields = ('city','last_updated')

