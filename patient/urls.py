from django.urls import path
from .import views

urlpatterns = [

    path('<int:pk>/', views.dashboard, name='dashboard'),
    path('update_patient_account/<int:pk>/', views.update_patient_account, name = 'update_patient_account'),
    path('appointment/<int:pk>/', views.appointment, name = 'appointment'),
    path('billing/<int:pk>/', views.billing, name = 'billing'),
    path('make_appointment/<int:pk>/', views.make_appointment, name = 'make_appointment'),
    path('view_appointment/<int:ap_id>/', views.view_appointment, name = 'view_appointment'),
    path('view_treatment/<int:treat_id>/', views.view_treatment, name='view_treatment'),
    path('view_labresult/<int:test_id>/', views.view_labresult, name='view_labresult'),
    path('getdoctor/', views.getdoctor, name = 'getdoctor'),

]