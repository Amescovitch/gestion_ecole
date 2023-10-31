from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField
from django import forms
from .models import *

class FormulaireConnexion(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom d\'utilisateur'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'}))
    captcha = CaptchaField()