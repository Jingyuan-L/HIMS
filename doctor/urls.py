from django.urls import path
from .import views


urlpatterns = [
    path('<int:pk>/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doc_view_appointment/<int:ap_id>/', views.doc_view_appointment, name='doc_view_appointment'),
    path('treat/<int:ap_id>/', views.treat, name='treat'),
    path('geticd/', views.geticd, name = 'geticd'),
    path('test/', views.test, name = 'test'),
]