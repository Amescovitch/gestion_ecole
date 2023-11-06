from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, nom, prenom, sexe, username, email, password):
        user = self.model(
            nom=nom,
            prenom=prenom,
            sexe=sexe,
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nom, prenom, sexe, username, email, password):
        user = self.create_user(
            nom=nom,
            prenom=prenom,
            sexe=sexe,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    SEXE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, default='M')
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Attributs spécifiques à la classe Professeur
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    classes_en_charges = models.ManyToManyField('Classe', through='ClasseMatiereProfesseur', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nom', 'prenom', 'email', 'sexe']

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class AnneeAcademique(models.Model):
    annee_debut = models.IntegerField()
    annee_fin = models.IntegerField()

    def __str__(self):
        return f"{self.annee_debut}-{self.annee_fin}"

class TrancheAcademique(models.Model):
    code = models.PositiveIntegerField()
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle

class Matiere(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class Eleve(models.Model):
    image = models.ImageField(upload_to='eleve_images/', null=True, blank=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50) 
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=Utilisateur.SEXE_CHOICES)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE, null=True, blank=True)
    parent1 = models.CharField(max_length=50, default='')
    parent2 = models.CharField(max_length=50, default='', blank=True, null=True)
    contact_parent1 = PhoneNumberField(default='')
    contact_parent2 = PhoneNumberField(blank=True, null=True)
    date_entree_etablissement = models.DateField(null=True, blank=True)
    observation = models.TextField(default='', blank=True,)
    nationalite = models.CharField(max_length=50, default='')
    adresse = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Classe(models.Model):
    code = models.CharField(max_length=10, unique=True)
    libelle = models.CharField(max_length=25, unique=True)
    titulaire = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True)
    est_semestre = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class ClasseMatiereProfesseur(models.Model):
    professeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    tranche_academique = models.ForeignKey(TrancheAcademique, on_delete=models.CASCADE)
    coefficient = models.PositiveIntegerField()

class NoteEvaluation(models.Model):
    note_classe = models.FloatField(null=True, blank=True)
    note_devoir = models.FloatField(null=True, blank=True)
    note_composition = models.FloatField(null=True, blank=True)
    moyenne_sur_20 = models.FloatField(null=True, blank=True)
    coefficient = models.PositiveIntegerField(blank=True, default=None)
    note_definitive = models.FloatField(null=True, blank=True)
    rang = models.CharField(max_length=10, blank=True, null=True, default='----nc----')
    appreciation = models.CharField(max_length=50, blank=True, null=True, default='----nc----')
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE, null=True, blank=True, default=None)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    tranche_academique = models.CharField(max_length=100, default="")
    professeur = models.ForeignKey('Utilisateur', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} - {self.annee_academique} - {self.tranche_academique}"
    
    def formatted_devoir(self):
            return '{:.2f}'.format(self.note_devoir) if self.note_devoir is not None else ''

    def formatted_composition(self):
        return '{:.2f}'.format(self.note_composition) if self.note_composition is not None else ''

    def formatted_moyenne_sur_20(self):
        return '{:.2f}'.format(self.moyenne_sur_20) if self.moyenne_sur_20 is not None else ''
    
    def formatted_classe(self):
            return '{:.2f}'.format(self.note_classe) if self.note_classe is not None else ''

    def formatted_note_definitive(self):
        return '{:.2f}'.format(self.note_definitive) if self.note_definitive is not None else ''