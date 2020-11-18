from django.shortcuts import render
#Importing UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .heart_disease import heart_disease_ml

# Create your views here.
def home(request):
	context = {}
	return render(request,'webapp/home.html',context)


def registerpage(request):
	context = {}
	return render(request,'webapp/register.html',context)


def loginpage(request):
	context = {}
	return render(request,'webapp/login.html',context)


def logoutpage(request):
	context = {}
	return redirect('login')


def user(request):
	context = {}
	return render(request,'webapp/user.html',context)


def create_patient(request):
	context = {}
	return render(request,'webapp/patient_form.html',context)


def update_patient(request):
	context = {}
	return render(request,'webapp/patient_form.html',context)


def delete_patient(request):
	context = {}
	return render(request,'webapp/delete.html',context)


def patient(request):
	context = {}
	return render(request,'webapp/patient.html',context)

def heart_disease(request):
	if request.method == 'POST':
		dic = request.POST
		X_encoded = heart_disease_ml.preprocess(dic)
		pred = heart_disease_ml.predict_disease(X_encoded)
		context = {'pred':pred}
		print(pred)
		render(request,'webapp/result.html',context)

	context = {}

	return render(request,'webapp/heart_disease.html',context)


def result(request):
	context = {}
	return render(request,'webapp/result.html',context)


