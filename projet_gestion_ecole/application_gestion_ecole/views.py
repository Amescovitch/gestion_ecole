from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from datetime import date
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

def saisie_notes_classe(request, classe_id, matiere_id):
    utilisateur = request.user
    classe = get_object_or_404(Classe, id=classe_id)
    matiere = get_object_or_404(Matiere, id=matiere_id)

    annee_academique_en_cours = AnneeAcademique.objects.filter(
        annee_debut__lte=date.today().year,
        annee_fin__gte=date.today().year
    ).first()

    coefficient = ClasseMatiereProfesseur.objects.filter(
        classe=classe,
        matiere=matiere,
    ).first().coefficient

    effectif = Eleve.objects.filter(classe=classe).count()

    if classe.est_semestre:
        tranche_academique = "Premier semestre"
    else:
        tranche_academique = "Premier trimestre"

    eleves = Eleve.objects.filter(classe=classe)
    notes_evaluation = NoteEvaluation.objects.filter(
        classe=classe,
        matiere=matiere,
    ).select_related('eleve')

    if request.method == 'POST':
        for eleve in classe.eleve_set.all():
            note_classe = request.POST.get(f"note_classe{eleve.id}")
            note_devoir = request.POST.get(f"note_devoir{eleve.id}")
            note_composition = request.POST.get(f"note_composition{eleve.id}")
            moyenne_sur_20 = request.POST.get(f"moyenne_sur_20{eleve.id}")
            coefficient = request.POST.get(f"coefficient{eleve.id}")
            note_definitive = request.POST.get(f"note_definitive{eleve.id}")
            rang = request.POST.get(f"rang{eleve.id}")
            appreciation = request.POST.get(f"appreciation{eleve.id}")

            note, created = NoteEvaluation.objects.get_or_create(
                eleve=eleve,
                matiere=matiere,
                classe=classe,
                defaults={
                    "note_classe": note_classe,
                    "note_devoir": note_devoir,
                    "note_composition": note_composition,
                    "moyenne_sur_20": moyenne_sur_20,
                    "coefficient": coefficient,
                    "note_definitive": note_definitive,
                    "rang": rang,
                    "appreciation": appreciation,
                    "annee_academique": annee_academique_en_cours,
                    "tranche_academique": tranche_academique,
                }
            )
            if not created:
                note.note_classe = note_classe
                note.note_devoir = note_devoir
                note.note_composition = note_composition
                note.moyenne_sur_20 = moyenne_sur_20
                note.coefficient = coefficient
                note.note_definitive = note_definitive
                note.rang = rang
                note.appreciation = appreciation
                note.save()

        return redirect('application_gestion_ecole:saisie_notes_classe', classe_id=classe_id, matiere_id=matiere_id)
    else:
        context = {
            'eleves': eleves,
            'notes_evaluation': notes_evaluation,
            'classe': classe,
            'matiere': matiere,
            'annee_academique_en_cours': annee_academique_en_cours,
            'coefficient': coefficient,
            'effectif': effectif,
            'tranche_academique': tranche_academique,
        }
        return render(request, 'saisie_notes_classe.html', context)