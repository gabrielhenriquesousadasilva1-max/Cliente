from .models import Cliente
from django import forms
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    nascimento = forms.CharField(widget=forms.DateInput(attrs={"class":"form-control", "type": "date"}))
    
    class Meta:
        model = Cliente
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']