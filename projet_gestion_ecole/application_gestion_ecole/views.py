from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def connexion(request):
    error_message = ''

    if request.method == 'POST':
        form = FormulaireConnexion(request.POST)

        # Vérifier si le formulaire est valide et si le CAPTCHA est correct
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            # Si l'authentification réussit, connectez l'utilisateur
            if user is not None:
                login(request, user)
                return redirect('application_gestion_ecole:tableau_de_bord')
            else:
                # Identifiants incorrects, définir un message d'erreur
                error_message = 'Nom d\'utilisateur et/ou mot de passe incorrect(s).'
        else:
            # CAPTCHA incorrect, définir un message d'erreur
            error_message = 'Le formulaire est invalide. Veuillez corriger les erreurs.'

    else:
        form = FormulaireConnexion()

    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'index.html', context)

def tableau_de_bord(request):
    return render(request, 'tableau_de_bord.html')

def classe_notes(request, classe_id):
    classe = Classe.objects.get(pk=classe_id)
    
    # Récupérer les professeurs associés à la classe
    professeurs = Utilisateur.objects.filter(classes_en_charges=classe)

    # Récupérer les élèves associés aux professeurs
    eleves = Eleve.objects.filter(classe=classe, professeur__in=professeurs)

    # Récupérer les notes associées à ces élèves
    notes = NoteEvaluation.objects.filter(eleve__in=eleves)

    context = {
        'classe': classe,
        'eleves': eleves,
        'notes': notes,
    }

    return render(request, 'classe_notes.html', context)
