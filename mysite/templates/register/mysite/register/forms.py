from django import forms
from django.forms import TextInput
from .models import Account


class RegisterUser(forms.ModelForm):

    class Meta:
        model = Account
        exclude = ('acc_id','is_doctor')


class Login(forms.Form):

    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class Prescribe(forms.Form):

    email = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    medication = forms.CharField(max_length=200)
    frequency = forms.CharField(max_length=200)
    dosage = forms.CharField(max_length=200)
    exp_date = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)




