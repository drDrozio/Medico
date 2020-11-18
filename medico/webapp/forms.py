from django.forms import ModelForm
from fdjango import forms

#User forms
from django.contrib.auth.forms import UserCreationForm
#Importing User from models
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']