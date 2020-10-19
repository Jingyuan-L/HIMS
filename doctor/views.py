from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone

import datetime

from patient.models import Patient,PatAppointment,Treatment,Doctor,Hospital,Ins_Pat,InsuranceProvider,OutPatient


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
