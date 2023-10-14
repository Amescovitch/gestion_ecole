from application_gestion_ecole.models import ClasseMatiereProfesseur

def classes_en_charge(request):
    classes_en_charge = []
    if request.user.is_authenticated:
        classes_en_charge = ClasseMatiereProfesseur.objects.filter(professeur=request.user).values_list('classe__libelle', flat=True).distinct()
    return {'classes_en_charge': classes_en_charge}
