from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from .models import Patient, PatAppointment, Treatment, Doctor, Hospital, Ins_Pat, InsuranceProvider, OutPatient, \
                    Billing, Lab, LabResult, IcdTable, InPatient, NursHmPatient, Receipt
from .forms import patientform


# from account import urls

# Create your views here.
@login_required(login_url='patient_login')
def dashboard(request, pk):
    patient = Patient.objects.get(p_id=pk)

    context = {
        'patient': patient
    }
    return render(request, 'patient/dashboard.html', context)


@login_required(login_url='patient_login')
def update_patient_account(request, pk):
    patient = Patient.objects.get(p_id=pk)

    p_form = patientform(instance=patient)

    if request.method == 'POST':
        p_form = patientform(request.POST)
        if p_form.is_valid():
            email_get = p_form.cleaned_data['e_mail']
            phone_get = p_form.cleaned_data['phone']
            firstname_get = p_form.cleaned_data['first_name']
            lastname_get = p_form.cleaned_data['last_name']
            state_get = p_form.cleaned_data['state']
            city_get = p_form.cleaned_data['city']
            streetaddress_get = p_form.cleaned_data['street_address']
            zipcode_get = p_form.cleaned_data['zip_code']

            patient = Patient.objects.filter(p_id=pk)
            patient.update(p_id=pk, e_mail=email_get, phone=phone_get, state=state_get, city=city_get,
                           first_name=firstname_get, last_name=lastname_get,
                           street_address=streetaddress_get, zip_code=zipcode_get)
            # 触发时间更新
            patient = Patient.objects.get(p_id=pk)
            patient.phone = phone_get
            patient.save()
            return redirect('update_patient_account', pk=pk)

    context = {
        'p_form': p_form,
        'patient': patient
    }
    return render(request, 'patient/update_patient_account.html', context)


@login_required(login_url='patient_login')
def appointment(request, pk):
    appointment = PatAppointment.objects.filter(p_id=pk, status='processing')
    patient = Patient.objects.get(p_id=pk)
    context = {
        'patient': patient,
        'appointment': appointment,
        'p_id': pk
    }
    return render(request, 'patient/appointment.html', context)


@login_required(login_url='patient_login')
def billing(request, pk):
    patient = Patient.objects.get(p_id=pk)
    appointments = PatAppointment.objects.filter(p_id=pk)
    treatments = []
    for apnt in appointments:
        treatments.extend(list(Treatment.objects.filter(ap_id=apnt.ap_id)))
    billings = []
    for treat in treatments:
        billings.extend(list(Billing.objects.filter(treat_id=treat.treat_id)))


    context = {
        'billings': billings,
        'patient': patient
    }
    return render(request, 'patient/billing.html', context)


@login_required(login_url='patient_login')
def view_receipt(request, b_id):
    billing = Billing.objects.get(b_id=b_id)
    receipt = Receipt.objects.get(b=billing)
    treat = Treatment.objects.get(billing=billing)
    app = PatAppointment.objects.get(ap_id=treat.ap.ap_id)
    patient = Patient.objects.get(p_id=app.p_id.p_id)

    context = {
        'billing': billing,
        'receipt': receipt,
        'patient': patient,
        'p_id': patient.p_id
    }
    return render(request, 'patient/view_receipt.html', context)


@login_required(login_url='patient_login')
def pay_bill(request, b_id):
    billing = Billing.objects.get(b_id=b_id)
    treat = Treatment.objects.get(billing=billing)
    app = PatAppointment.objects.get(ap_id=treat.ap.ap_id)
    patient = Patient.objects.get(p_id=app.p_id.p_id)


    if request.method == "POST":
        method = request.POST.get('pay_method')
        new_receipt = Receipt.objects.create(b=billing, payment_amout=billing.amount,
                                             payment_date=datetime.datetime.now(), pay_method=method,
                                             tbl_last_dt=datetime.datetime.now())
        new_receipt.save()
        billing.paid = True
        billing.save()
        print("post payment")
        return redirect('view_receipt', b_id=b_id)

    context = {
        'billing': billing,
        'patient': patient,
        'p_id': patient.p_id,
        'b_id': b_id
    }
    return render(request, 'patient/pay_bill.html', context)


@login_required(login_url='patient_login')
def view_appointment(request, ap_id):
    appointment = PatAppointment.objects.get(ap_id=ap_id)
    patient = Patient.objects.get(p_id=appointment.p_id.p_id)
    treatment = Treatment.objects.filter(ap_id=ap_id)
    inpatient, outpatient, nursinghome = None, None, None
    if appointment.type == 'inpatient':
        inpatient = InPatient.objects.get(ap_id=ap_id)
    elif appointment.type == 'outpatient':
        outpatient = OutPatient.objects.get(ap_id=ap_id)
    elif appointment.type == 'nursinghome':
        nursinghome = NursHmPatient.objects.get(ap_id=ap_id)
    context = {
        'patient': patient,
        'appointment': appointment,
        'treatment': treatment,
        'inpatient': inpatient,
        'outpatient': outpatient,
        'nursinghome': nursinghome
    }
    return render(request, 'patient/view_appointment.html', context)


@login_required(login_url='patient_login')
def view_treatment(request, treat_id):
    treatment = Treatment.objects.get(treat_id=treat_id)
    appointment = PatAppointment.objects.get(ap_id=treatment.ap.ap_id)
    lab_results = LabResult.objects.filter(treat_id=treat_id)

    context = {
        'lab_results': lab_results,
        'appointment': appointment,
        'treatment': treatment
    }
    return render(request, 'patient/view_treatment.html', context)


@login_required(login_url='patient_login')
def view_labresult(request, test_id):
    lab_result = LabResult.objects.get(test_id=test_id)
    lab = Lab.objects.get(lab_id=lab_result.lab.lab_id)

    context = {
        'lab_results': lab_result,
        'lab': lab
    }
    return render(request, 'patient/view_labresult.html', context)


@login_required(login_url='patient_login')
def make_appointment(request, pk):
    patient = Patient.objects.get(p_id=pk)
    context = {
        'patient': patient
    }
    if request.method == "POST":
        seldoctor_get = request.POST.get('seldoctor')
        treat_time_get = request.POST.get('treated_time')
        insname_get = request.POST.get('ins')
        print(request.POST)
        doctor = Doctor.objects.get(first_name=seldoctor_get)
        inp = InsuranceProvider.objects.get(ins_provider_name__startswith=insname_get)
        new_ap = PatAppointment.objects.create(doctor=doctor, type='outpatient', status='processing',
                                               ins_p_id=inp, p_id=patient)
        new_ap.save()
        new_out = OutPatient.objects.create(ap_id=new_ap, treated_time=treat_time_get)
        new_out.save()
        return redirect('appointment', pk=pk)
    else:
        try:
            have_ins = Ins_Pat.objects.filter(p_id=pk)
            inslist = []
            for inp in have_ins:
                inslist.append(inp.ins_p_id.ins_provider_name)
            hospitallist = Hospital.objects.all().values("hospital_name").distinct()
            context['hospitallist'] = hospitallist
            context['inslist'] = inslist
        except Exception:
            context['login_err'] = 'login_err'
            return render(request, "patient/make_appointment.html", context)

        return render(request, "patient/make_appointment.html", context)


@login_required(login_url='patient_login')
def getdoctor(request):
    if request.method == 'GET':
        selhospital = request.GET.get('selhospital')
        if selhospital:
            data = list(Doctor.objects.filter(hospital__hospital_name=selhospital).values('first_name'))
            return JsonResponse(data, safe=False)
