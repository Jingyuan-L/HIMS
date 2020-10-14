from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import Patient
from .forms import patientform
#from account import urls

# Create your views here.
@login_required(login_url='patient_login')
def dashboard(request, pk):
    patient = Patient.objects.get(p_id=pk)

    context = {
        'patient':patient
    }
    return render(request, 'patient/dashboard.html',context)

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
            patient.update(p_id=pk, e_mail=email_get,phone=phone_get, state = state_get, city = city_get,
                           first_name = firstname_get, last_name = lastname_get,
                           street_address =streetaddress_get, zip_code = zipcode_get)
            #触发时间更新
            patient = Patient.objects.get(p_id = pk)
            patient.phone = phone_get
            patient.save()
            return redirect('update_patient_account', pk = pk)

    context = {
        'p_form': p_form,
        'patient': patient
    }
    return render(request, 'patient/update_patient_account.html', context)

@login_required(login_url='patient_login')
def appointment(request, pk):
    patient = Patient.objects.get(p_id=pk)

    context = {
        'patient': patient
    }
    return render(request, 'patient/appointment.html', context)