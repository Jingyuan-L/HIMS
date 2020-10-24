from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from random import choice
from dateutil.relativedelta import relativedelta

import datetime

from patient.models import Patient,PatAppointment,Treatment,Doctor,Hospital,Ins_Pat,InsuranceProvider,\
    OutPatient,IcdTable,InPatient,NursHmPatient,LabResult,Lab,Billing,Room


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
    if request.method == "POST":
        icd_get = request.POST.get('icd')
        description_get = request.POST.get('description')
        type_get = request.POST.get('treat_type')
        icd = IcdTable.objects.get(icd_code=icd_get)
        new_treatment = Treatment.objects.create(description=description_get, icd_code=icd, ap_id=ap_id,treat_type=type_get,tbl_last_dt=datetime.datetime.now())
        new_treatment.save()
        new_billing = Billing.objects.create(amount=1000, treat=new_treatment, due_date=datetime.date.today() - relativedelta(months=+1),paid=False,tbl_last_dt=datetime.datetime.now())
        new_billing.save()
        return redirect('doc_view_appointment', ap_id=ap_id)

    context = {
        'doctor': doctor,
        'appointment': appointment,
    }
    return render(request, 'doctor/treat.html', context)

@login_required(login_url='doctor_login')
def doc_view_treatment(request, treat_id):
    treatment = Treatment.objects.get(treat_id=treat_id)
    appointment = PatAppointment.objects.get(ap_id=treatment.ap.ap_id)
    lab_results = LabResult.objects.filter(treat_id=treat_id)
    doctor = appointment.doctor

    context = {
        'lab_results': lab_results,
        'appointment': appointment,
        'treatment': treatment,
        'doctor':doctor
    }
    return render(request, 'doctor/doc_view_treatment.html', context)

@login_required(login_url='doctor_login')
def geticd(request):
    if request.method == 'GET':
        icd = request.GET.get('icd')
        if icd:
            data = list(IcdTable.objects.filter(icd_code__startswith=icd).values('icd_code','description'))
            return JsonResponse(data, safe=False)


@login_required(login_url='doctor_login')
def make_labtest(request, treat_id):
    treat = Treatment.objects.get(treat_id=treat_id)
    doctor = treat.ap.doctor
    lablist = Lab.objects.all().values("lab_name").distinct()
    result = ['positive', 'negative']
    context = {
        'treat':treat,
        'doctor': doctor,
        'lablist':lablist
    }
    if request.method == "POST":
        lab_get = request.POST.get('lab')
        description_get = request.POST.get('description')
        lab = Lab.objects.get(lab_name=lab_get)
        LabResult.objects.create(test_description=description_get, test_result=choice(result), lab=lab, treat=treat, tbl_last_dt=(datetime.datetime.now()))
        return redirect('doc_view_treatment', treat_id=treat_id)
    return render(request, 'doctor/make_labtest.html', context)

@login_required(login_url='doctor_login')
def doc_make_outpatient(request, ap_id):
    old_ap = PatAppointment.objects.get(ap_id=ap_id)
    doctor = old_ap.doctor
    context = {
        'old_ap':old_ap,
        'doctor': doctor,
    }
    if request.method == "POST":
        treat_time_get = request.POST.get('treated_time')
        old_ap.status = 'further operation'
        old_ap.save()
        new_ap = PatAppointment.objects.create(ap_time=datetime.datetime.now(), tbl_last_dt=datetime.datetime.now(),
                                               doctor=doctor, ins_p_id=old_ap.ins_p_id, last_ap=old_ap, p_id=old_ap.p_id,
                                               type='outpatient', status='processing')
        new_ap.save()
        new_out = OutPatient.objects.create(ap_id=new_ap, treated_time=treat_time_get)
        new_out.save()
        return redirect('doctor_dashboard', pk=doctor.doctor_id)
    return render(request, 'doctor/doc_make_outpatient.html', context)

@login_required(login_url='doctor_login')
def doc_make_nursinghome(request, ap_id):
    old_ap = PatAppointment.objects.get(ap_id=ap_id)
    doctor = old_ap.doctor
    context = {
        'old_ap':old_ap,
        'doctor': doctor,
    }
    if request.method == "POST":
        end_time_get = request.POST.get('end_time')
        old_ap.status = 'further operation'
        old_ap.save()
        new_ap = PatAppointment.objects.create(ap_time=datetime.datetime.now(), tbl_last_dt=datetime.datetime.now(),
                                               doctor=doctor, ins_p_id=old_ap.ins_p_id, last_ap=old_ap, p_id=old_ap.p_id,
                                               type='nursinghome', status='processing')
        new_ap.save()
        new_nurs = NursHmPatient.objects.create(ap_id=new_ap, start_time=datetime.datetime.now(), end_time=end_time_get,
                                                tbl_last_dt=datetime.datetime.now())
        new_nurs.save()
        return redirect('doctor_dashboard', pk=doctor.doctor_id)
    return render(request, 'doctor/doc_make_nursinghome.html', context)

@login_required(login_url='doctor_login')
def doc_make_inpatient(request, ap_id):
    old_ap = PatAppointment.objects.get(ap_id=ap_id)
    doctor = old_ap.doctor
    room_list = Room.objects.filter(occupied=False, hospital=doctor.hospital)
    context = {
        'old_ap': old_ap,
        'doctor': doctor,
        'room_list': room_list
    }
    if request.method == "POST":
        end_time_get = request.POST.get('end_time')
        room_get = request.POST.get('room')
        old_ap.status = 'further operation'
        old_ap.save()
        new_ap = PatAppointment.objects.create(ap_time=datetime.datetime.now(), tbl_last_dt=datetime.datetime.now(),
                                               doctor=doctor, ins_p_id=old_ap.ins_p_id, last_ap=old_ap, p_id=old_ap.p_id,
                                               type='inpatient', status='processing')
        new_ap.save()
        room = Room.objects.get(room_name=room_get, hospital=doctor.hospital)
        room.occupied = True
        room.save()
        new_inpatient = InPatient.objects.create(ap_id=new_ap, start_time=datetime.datetime.now(), end_time=end_time_get,
                                                tbl_last_dt=datetime.datetime.now(),room=room)
        new_inpatient.save()
        return redirect('doctor_dashboard', pk=doctor.doctor_id)
    return render(request, 'doctor/doc_make_inpatient.html', context)

def test(request):
    return render(request, 'doctor/text.html')
