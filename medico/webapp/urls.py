from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('result/',views.result,name='result'),

    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.registerpage,name='registerpage'),
    path('logout/',views.logoutpage,name='logoutpage'),	

    path('patient_form/',views.patient_form,name='patient_form'),
    path('update_patient/',views.update_patient,name='update_patient'),
    path('delete_patient/',views.delete_patient,name='delete_patient'),

    path('user/<str:pk>/',views.userpage,name='userpage'),
    path('patient/<str:pk_test>/',views.patient,name='patient'),

    path('heart_disease/',views.heart_disease,name='heart_disease'),
    path('covid/',views.covid,name='covid'),

]