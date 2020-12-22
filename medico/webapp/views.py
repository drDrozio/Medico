from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
#Importing UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import DetailsForm, CreateUserForm
#Decorators for user roles
from .decorators import unauthenticated_user, admin_it_only
from .heart_disease import heart_disease_ml
from .covid_preprocess import preprocess
from .liver import liver_preprocess
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from tensorflow import Graph

# Create your views here.
@login_required(login_url='loginpage')
def home(request):
	patient = Patient.objects.all()
	total_patients = patient.count()

	#Testing tf
	a=tf.constant(7)
	b=tf.constant(10)
	c = tf.add(a,b)
	print(c)

	context = {'total_patients' : total_patients, 'patient':patient}
	return render(request,'webapp/home.html',context)


@unauthenticated_user
def registerpage(request):
	form = CreateUserForm(request.POST)
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

			user = form.save()
			username =  form.cleaned_data.get("username")

			group = Group.objects.get(name='patients')
			user.groups.add(group)
			Patient.objects.create(user=user)

			messages.success(request,'Account created for ' + user)
			return redirect('loginpage')
	context = {'form' : form}
	return render(request,'webapp/register.html',context)


@unauthenticated_user
def loginpage(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username or password is incorrect')

	context = {}
	return render(request,'webapp/login.html',context)


def logoutpage(request):
	logout(request)
	return redirect('loginpage')

@login_required(login_url='loginpage')
def userpage(request,pk):
	pk=request.user.patient.id
	patient = Patient.objects.filter(id=int(pk)).first()
	print(patient)
	details = patient.details_set.all()

	context = {'patient':patient, 'details': details}
	return render(request,'webapp/user.html',context)

@login_required(login_url='loginpage')
def patient_form(request):
	form = DetailsForm()
	if request.method == 'POST':
		form = DetailsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form' : form}
	return render(request,'webapp/patient_form.html',context)


def update_patient(request):
	# patient = Patient.objects.get(id=pk)
	# form = DetailsForm(instance=patient)
	# if request.method == 'POST':
	# 	form = DetailsForm(request.POST,instance=patient)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('/')
	# context = {'form' : form}
	context = {}
	return render(request,'webapp/patient_form.html',context)

@admin_it_only
def delete_patient(request):
	context = {}
	return render(request,'webapp/delete.html',context)


def patient(request):
	context = {}
	return render(request,'webapp/patient.html',context)

@login_required(login_url='loginpage')
def heart_disease(request):
	if request.method == 'POST':
		dic = request.POST
		X_encoded = heart_disease_ml.preprocess(dic)
		pred = heart_disease_ml.predict_disease(X_encoded)

		if pred<=1:
			advise = 'Your heart seems to be in good condition. You are good to go!'
		elif pred>=3:
			advise = 'Your heart is not in a good condition. You are advised to consult a Physician'
		else:
			advise = 'Your heart is still OK but we advise you to take care and stay healthy'

		context = {'pred':pred, 'advise' : advise}
		print("Prediction : ",pred)
		return render(request,'webapp/result.html',context)

	context = {}
	return render(request,'webapp/heart_disease.html',context)

def covid(request):
	#prediction = pred(X)
	if request.method == 'POST':
		print(request.POST)
		print (request.POST.dict())
		fileObj=request.FILES['filePath']
		fs=FileSystemStorage()
		filePathName=fs.save(fileObj.name,fileObj)
		filePathName=fs.url(filePathName)
		context={'filePathName':filePathName}
		return render(request,'webapp/covid_form.html',context) 
		#print(preprocess())
	context = {}
	return render(request,'webapp/covid_form.html',context)

def liver(request):
	return liver_preprocess()

@login_required(login_url='loginpage')
def result(request):
	context = {}
	return render(request,'webapp/result.html',context)


