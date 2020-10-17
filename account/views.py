from patient.models import Patient
from patient import urls
from .forms import RegisterForm

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

#from .models import
#from .forms import
# Create your views here.

def homepage(request):
    return render(request, 'account/homepage.html')

def patient_login(request):
    if request.user.is_authenticated:
        current_user = request.user
        current_patient = Patient.objects.get(user = current_user.id)
        return redirect('dashboard', pk = current_patient.p_id)
    else:
        message = ''
        if request.method == 'POST':
            username_get = request.POST.get('username')
            pwd_get = request.POST.get('password')

            user = authenticate(request, username = username_get, password=pwd_get)
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
            'message' : message
        }

    return render(request, 'account/patient_login.html', context)

def logout_user(request):
    logout(request)
    return redirect('homepage')

def doctor_login(request):
    return render(request, 'account/doctor_login.html')

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
                    new_user = User.objects.create_user(username=username_get, password=pwd1_get,email=email_get)
                    new_user.save()
                    Patient.objects.create(user= new_user, e_mail=email_get)
                    return redirect('patient_login')
                else:
                    message = 'different password'
            except:
                message = 'username or email has been occupied'
                #new_user.delete()

    context = {
        'r_form':r_form,
        'message':message
    }
    return render(requset, 'account/register.html', context)
