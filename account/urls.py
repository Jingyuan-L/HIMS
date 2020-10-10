from django.urls import path
from .import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('patient_login/',views.patient_login, name='patient_login'),
    path('doctor_login/',views.doctor_login, name='doctor_login'),
    path('register/', views.register, name='register')
]