from django.contrib import admin
from .models import *

# Modifier le titre de l'administration ici
admin.site.site_title = "Accueil Admin"
admin.site.site_header = "Administration Gestion Ecole"
admin.site.index_title = "Tableau de bord"

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'sexe', 'username', 'email', 'is_staff', 'id']
    search_fields = ['id', 'nom', 'username']
admin.site.register(Utilisateur, UtilisateurAdmin)