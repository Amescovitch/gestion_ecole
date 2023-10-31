from application_gestion_ecole.models import ClasseMatiereProfesseur

# Exemple de context processor
def classes_en_charge(request):
    classes_en_charge = []

    if request.user.is_authenticated:
        # Filtrer les classes avec ID non nul
        classes_en_charge = ClasseMatiereProfesseur.objects.filter(
            professeur=request.user,
            classe__id__isnull=False
        ).values('classe__id', 'classe__libelle', 'matiere__id', 'matiere__code').distinct()

    return {'classes_en_charge': classes_en_charge}
