from django.core import validators
from django import forms
from django.forms import fields, models, widgets
from django.shortcuts import render
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','address','number','gender']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),

        }