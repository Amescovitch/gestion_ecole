from django.contrib import admin
from .models import *

# Modifier le titre de l'administration ici
admin.site.site_title = "Accueil Admin"
admin.site.site_header = "Administration Gestion Ecole"
admin.site.index_title = "Tableau de bord"

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'sexe', 'username', 'email', 'is_staff', 'code', 'display_classes_en_charges']

    def display_classes_en_charges(self, obj):
        return ", ".join([classe.code for classe in obj.classes_en_charges.all()])

    display_classes_en_charges.short_description = 'classes_en_charges'
    
@admin.register(AnneeAcademique)
class AnneeAcademiqueAdmin(admin.ModelAdmin):
    list_display = ['annee_debut', 'annee_fin']

@admin.register(TrancheAcademique)
class TrancheAcademiqueAdmin(admin.ModelAdmin):
    list_display = ['code', 'libelle']

@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ['code', 'nom', 'id']

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'date_naissance', 'sexe', 'classe']

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ['code', 'libelle', 'est_semestre', 'titulaire', 'id']

@admin.register(ClasseMatiereProfesseur)
class ClasseMatiereProfesseurAdmin(admin.ModelAdmin):
    list_display = ['professeur', 'classe', 'matiere', 'annee_academique', 'tranche_academique', 'coefficient']

@admin.register(ClasseEleve)
class ClasseEleveAdmin(admin.ModelAdmin):
    list_display = ['classe', 'display_eleves']

    def display_eleves(self, obj):
        return ", ".join([eleve.nom for eleve in obj.eleve.all()])

    display_eleves.short_description = 'Élèves'

@admin.register(NoteEvaluation)
class NoteEvaluationAdmin(admin.ModelAdmin):
    list_display = ['annee_academique', 'tranche_academique', 'classe', 'matiere', 'eleve', 'note_classe', 'note_devoir', 'note_composition', 'moyenne_sur_20', 'note_definitive', 'rang', 'appreciation']
