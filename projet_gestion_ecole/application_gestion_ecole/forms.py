from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class FormulaireConnexion(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom d\'utilisateur'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'}))
    captcha = CaptchaField()

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = '__all__'

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'date_naissance': DateInput(attrs={'class': 'form-control', 'required': 'required'}),
            'sexe': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'classe': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'parent1': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'contact_parent1': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'type': 'tel'}),
            'date_entree_etablissement': DateInput(attrs={'class': 'form-control', 'required': 'required'}),
            'nationalite': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'parent2': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_parent2': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'observation': forms.Textarea(attrs={'class': 'form-control', 'rows':2}),
        }
