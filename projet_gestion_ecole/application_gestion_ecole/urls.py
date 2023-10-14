from application_gestion_ecole.views import *
from django.urls import path

app_name = 'application_gestion_ecole'
urlpatterns = [
    #connexion  
    path('', connexion, name="index"),

    #tableaux de bord
    path('tableau_de_bord/', tableau_de_bord, name="tableau_de_bord"),

    #classe note
    path('classe/<int:classe_id>/notes/', classe_notes, name='classe_notes'),


    #réinitialisation de mot de passe
    #path('password_reset/', custom_auth_views.custom_password_reset, name='password_reset'),
    #path('password_reset/done/', custom_auth_views.custom_password_reset_done, name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', custom_auth_views.custom_password_reset_confirm, name='password_reset_confirm'),
    #path('reset/done/', custom_auth_views.custom_password_reset_complete, name='password_reset_complete'),
]