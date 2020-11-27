from django.forms import ModelForm
from fdjango import forms
from .models import Patient

#User forms
from django.contrib.auth.forms import UserCreationForm
#Importing User from models
from django.contrib.auth.models import User

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'
		exclude = ['user']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']