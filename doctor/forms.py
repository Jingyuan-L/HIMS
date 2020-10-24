from patient.models import Doctor
from django import forms
from django.forms import ModelForm

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

        exclude = ['doctor_id', 'hiredate', 'tbl_last_dt', 'user', 'hospital']

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'please input your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'please input your last name'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'state'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'city'
            }),
            'street_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'street_address'
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'zip_code'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'phone'
            }),
            'e_mail': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e_mail'
            })
        }



