from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Statement

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15 )
    full_name = forms.CharField(max_length=200, required=True)
    city = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'full_name',
            'city',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            # 'full_name': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'ФИО'
            # }),
            # 'city': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'город'
            # }),
            # 'phone_number': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': '+7(XXX)-XXX-XX-XX'
            # }),
        }

        
        
class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = (
            'adress',
            'name',
            'description',
        )
        widgets = {
            'adress': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'адрес'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }