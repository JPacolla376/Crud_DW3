from datetime import date
from django import forms
from .models import Chamado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo', 'descricao', 'classificacao', 'data_vencimento', 'anexo']

    def clean_data_vencimento(self):
        data_vencimento = self.cleaned_data['data_vencimento']
        if data_vencimento and data_vencimento < date.today():
            raise forms.ValidationError("A data de vencimento não pode ser antes do dia atual.")
        return data_vencimento


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None  
