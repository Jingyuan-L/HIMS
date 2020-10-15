from django.urls import path
from .import views

urlpatterns = [


    path('<int:pk>/', views.dashboard, name='dashboard'),
    path('update_patient_account/<int:pk>/', views.update_patient_account, name = 'update_patient_account'),
    path('appointment/<int:pk>/', views.appointment, name = 'appointment'),
    path('view_appointment/<int:ap_id>/', views.view_appointment, name = 'view_appointment')
]