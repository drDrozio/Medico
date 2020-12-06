from django.forms import ModelForm
from django import forms
from .models import Details
#User forms
from django.contrib.auth.forms import UserCreationForm
#Importing User from models
from django.contrib.auth.models import User

class DetailsForm(ModelForm):
	class Meta:
		model = Details
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']