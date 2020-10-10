from django import forms
from django.forms import ModelForm
from .models import Patient

class patientform(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['p_id','register_date','tbl_last_dt','user']

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholedr': 'please input your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholedr': 'please input your last name'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholedr': 'state'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholedr': 'city'
            }),
            'street_address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholedr': 'street_address'
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholedr': 'zip_code'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholedr': 'phone'
            }),
            'e_mail': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholedr': 'e_mail'
            }),
            'member_insurance_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholedr': 'member_insurance_id'
            })
        }