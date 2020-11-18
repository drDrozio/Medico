from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
	patient = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	