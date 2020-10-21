from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone

import datetime

from patient.models import Patient,PatAppointment,Treatment,Doctor,Hospital,Ins_Pat,InsuranceProvider,OutPatient,IcdTable


# Create your views here.

@login_required(login_url='doctor_login')
def doctor_dashboard(request, pk):
    doctor = Doctor.objects.get(doctor_id=pk)
    today_ap = PatAppointment.objects.filter(doctor=pk, status='processing', type='outpatient')

    context = {
        'doctor':doctor,
        'today_ap':today_ap
    }
    return render(request, 'doctor/dashboard.html',context)


@login_required(login_url='doctor_login')
def doc_view_appointment(request, ap_id):
    appointment = PatAppointment.objects.get(ap_id=ap_id)
    doctor = appointment.doctor
    treatment = Treatment.objects.filter(ap_id=ap_id)
    inpatient, outpatient, nursinghome = None, None, None
    if appointment.type == 'inpatient':
        inpatient = InPatient.objects.get(ap_id=ap_id)
    elif appointment.type == 'outpatient':
        outpatient = OutPatient.objects.get(ap_id=ap_id)
    elif appointment.type == 'nursinghome':
        nursinghome = NursHmPatient.objects.get(ap_id=ap_id)
    context = {
        'doctor': doctor,
        'appointment': appointment,
        'treatment': treatment,
        'inpatient': inpatient,
        'outpatient': outpatient,
        'nursinghome': nursinghome
    }
    return render(request, 'doctor/doc_view_appointment.html', context)

@login_required(login_url='doctor_login')
def treat(request, ap_id):
    appointment = PatAppointment.objects.get(ap_id=ap_id)
    doctor = appointment.doctor
    context = {
        'doctor': doctor,
        'appointment': appointment,
    }
    return render(request, 'doctor/treat.html', context)

@login_required(login_url='doctor_login')
def geticd(request):
    if request.method == 'GET':
        icd = request.GET.get('icd')
        print(1)
        if icd:
            data = list(IcdTable.objects.filter(icd_code__startswith=icd).values('icd_code','description'))
            print(data[0])
            return JsonResponse(data, safe=False)
