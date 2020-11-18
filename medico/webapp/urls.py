from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('result/',views.result,name='result'),

    path('login/',views.loginpage,name='loginpage'),
    path('register/',views.registerpage,name='registerpage'),
    path('logout/',views.logoutpage,name='logoutpage'),	

    path('create_patient/<str:pk>/',views.create_patient,name='create_patient'),
    path('update_patient/<str:pk>/',views.update_patient,name='update_patient'),
    path('delete_patient/<str:pk>/',views.delete_patient,name='delete_patient'),

    path('user/',views.user,name='user'),
    path('patient/<str:pk_test>/',views.patient,name='patient'),

    path('heart_disease/',views.heart_disease,name='heart_disease'),
]