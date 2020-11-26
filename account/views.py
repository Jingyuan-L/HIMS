from patient.models import Patient, Doctor, Hospital
from patient import urls
from doctor import urls
from .forms import RegisterForm, DoctorRegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# from .models import
# from .forms import
# Create your views here.

def homepage(request):
    return render(request, 'account/homepage.html')


def patient_login(request):
    if request.user.is_authenticated:
        current_user = request.user
        try:
            current_patient = Patient.objects.get(user=current_user.id)
        except:
            message = 'You are not a PATIENT!'
            context = {
                'message': message
            }
            return render(request, 'account/patient_login.html', context)

        return redirect('dashboard', pk=current_patient.p_id)
    else:
        message = ''
        if request.method == 'POST':
            username_get = request.POST.get('username')
            pwd_get = request.POST.get('password')

            user = authenticate(request, username=username_get, password=pwd_get)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    current_user = request.user
                    current_patient = Patient.objects.get(user=current_user.id)
                    return redirect('dashboard', pk=current_patient.p_id)
                else:
                    message = 'account is not active'
            else:
                message = 'username or password wrong'

        context = {
            'message': message
        }

    return render(request, 'account/patient_login.html', context)


def logout_user(request):
    logout(request)
    return redirect('homepage')


def doctor_login(request):
    if request.user.is_authenticated:
        current_user = request.user
        try:
            current_doctor = Doctor.objects.get(user=current_user.id)
        except:
            message = 'You are not a DOCTOR!'
            context = {
                'message': message
            }
            return render(request, 'account/doctor_login.html', context)

        return redirect('doctor_dashboard', pk=current_doctor.doctor_id)
    else:
        message = ''
        if request.method == 'POST':
            username_get = request.POST.get('username')
            pwd_get = request.POST.get('password')

            user = authenticate(request, username=username_get, password=pwd_get)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    current_user = request.user
                    current_doctor = Doctor.objects.get(user=current_user.id)
                    return redirect('doctor_dashboard', pk=current_doctor.doctor_id)
                else:
                    message = 'account is not active'
            else:
                message = 'username or password wrong'

        context = {
            'message': message
        }

    return render(request, 'account/doctor_login.html', context)


def register(requset):
    r_form = RegisterForm()
    message = ''

    if requset.method == 'POST':
        r_form = RegisterForm(requset.POST)
        if r_form.is_valid():
            username_get = r_form.cleaned_data['username']
            pwd1_get = r_form.cleaned_data['password']
            pwd2_get = r_form.cleaned_data['password2']
            email_get = r_form.cleaned_data['email']

            try:
                if pwd1_get == pwd2_get:
                    new_user = User.objects.create_user(username=username_get, password=pwd1_get, email=email_get)
                    new_user.save()
                    Patient.objects.create(user=new_user, e_mail=email_get)
                    return redirect('patient_login')
                else:
                    message = 'different password'
            except:
                message = 'username or email has been occupied'
                # new_user.delete()

    context = {
        'r_form': r_form,
        'message': message
    }
    return render(requset, 'account/register.html', context)


def doc_register(requset):
    r_form = DoctorRegisterForm()
    message = ''

    if requset.method == 'POST':
        r_form = DoctorRegisterForm(requset.POST)
        if r_form.is_valid():
            username_get = r_form.cleaned_data['username']
            pwd1_get = r_form.cleaned_data['password']
            pwd2_get = r_form.cleaned_data['password2']
            email_get = r_form.cleaned_data['email']
            hospital_id = r_form.cleaned_data['hospital_id']
            hospital_id = hospital_id.hospital_id
            print(hospital_id)
            try:
                if pwd1_get == pwd2_get:
                    new_user = User.objects.create_user(username=username_get, password=pwd1_get, email=email_get)
                    new_user.save()
                    Doctor.objects.create(hospital_id=hospital_id, user=new_user, e_mail=email_get)
                    return redirect('doctor_login')
                else:
                    message = 'different password'
            except Exception:
                raise Exception
                message = 'username or email has been occupied'
                # new_user.delete()

    hospitallist = Hospital.objects.all().values("hospital_name").distinct()

    context = {
        'r_form': r_form,
        'message': message,
        'hospitallist': hospitallist
    }
    return render(requset, 'account/doc_register.html', context)
