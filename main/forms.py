from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Statement

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
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
        }


STATUSES = (
    ('Новый', 'Новый'),
    ('В обработке', 'В обработке'),
    ('Выполнен', 'Выполнен'),
)


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = [
            'adress',
            'name',
            'description',
        ]
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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and (user.is_superuser or user.is_staff):
            self.fields['status'] = forms.ChoiceField(choices=STATUSES, widget=forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус'
            }))