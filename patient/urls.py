from django.urls import path
from .import views

urlpatterns = [


    path('<int:pk>/', views.dashboard, name='dashboard'),
    path('update_patient_account/<int:pk>/', views.update_patient_account, name = 'update_patient_account')
]