from django.urls import path
from .import views


urlpatterns = [
    path('<int:pk>/', views.doctor_dashboard, name='doctor_dashboard'),

]