from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
	patientID = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	profile_pic = models.ImageField(default="logoo.png",null=True,blank=True)

	def __str__(self):
		return self.name

class Details(models.Model):
	SEX = (
			('Male','Male'),
			('Female','Female'),
			('Others','Others'),
			)

	BLOOD_GRP = (
					('A+','A+'),
					('A-','A-'),
					('AB+','AB+'),
					('AB-','AB-'),
					('B+','B+'),
					('B-','B-'),
					('O+','O+'),
					('O-','O-'),
				)

	patientID = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
	age = models.IntegerField(null=True)
	sex = models.CharField(max_length=10, null=True, choices=SEX)
	height = models.FloatField()
	weight = models.FloatField()
	bloodgrp = models.CharField(max_length=4, null=True, choices=BLOOD_GRP)
	BP = models.FloatField()
	temp = models.FloatField()
	history = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.patientID.name

