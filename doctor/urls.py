from django.urls import path
from .import views


urlpatterns = [
    path('<int:pk>/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doc_view_appointment/<int:ap_id>/', views.doc_view_appointment, name='doc_view_appointment'),
    path('treat/<int:ap_id>/', views.treat, name='treat'),
    path('geticd/', views.geticd, name = 'geticd'),
    path('test/', views.test, name = 'test'),
    path('doc_view_treatment/<int:treat_id>/', views.doc_view_treatment, name='doc_view_treatment'),
    path('make_labtest/<int:treat_id>/', views.make_labtest, name='make_labtest'),
    path('doc_make_outpatient/<int:ap_id>/', views.doc_make_outpatient, name='doc_make_outpatient'),
    path('doc_make_nursinghome/<int:ap_id>/', views.doc_make_nursinghome, name='doc_make_nursinghome'),
    path('doc_make_inpatient/<int:ap_id>/', views.doc_make_inpatient, name='doc_make_inpatient'),
]