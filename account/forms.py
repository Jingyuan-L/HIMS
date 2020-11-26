from django import forms
from patient.models import Hospital
from django.forms import ModelForm
from patient.models import Patient



class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'username'
        })
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'password'
        })
    )
    password2 = forms.CharField(
        max_length=100,
        label='password again',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'please input password again'
        })
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'email'
        })
    )

class DoctorRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'username'
        })
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'password'
        })
    )
    password2 = forms.CharField(
        max_length=100,
        label='password again',
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'please input password again'
        })
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'email'
        })
    )
    hospital_id = forms.ModelChoiceField(
        queryset=Hospital.objects.all()
    )
