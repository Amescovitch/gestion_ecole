from application_gestion_ecole.views import *
from django.urls import path

app_name = 'application_gestion_ecole'
urlpatterns = [
    path('', connexion, name="index"),

    path('tableau_de_bord/', tableau_de_bord, name="tableau_de_bord"),

    path('saisie-notes-classe/<int:classe_id>/<int:matiere_id>/', saisie_notes_classe, name='saisie_notes_classe'),
]   