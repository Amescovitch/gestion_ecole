from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
        return self.nom

class Eleve(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=Utilisateur.SEXE_CHOICES)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Classe(models.Model):
    code = models.CharField(max_length=10, unique=True)
    libelle = models.CharField(max_length=25, unique=True)
    titulaire = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.code

class ClasseMatiereProfesseur(models.Model):
    professeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    tranche_academique = models.ForeignKey(TrancheAcademique, on_delete=models.CASCADE)
    coefficient = models.FloatField()

class ClasseEleve(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleve = models.ManyToManyField(Eleve)

class Appreciation(models.Model):
    texte = models.CharField(max_length=50)
    intervalle_debut = models.FloatField()
    intervalle_fin = models.FloatField()

    def __str__(self):
        return self.texte

class NoteEvaluation(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee_academique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    tranche_academique = models.ForeignKey(TrancheAcademique, on_delete=models.CASCADE)
    note_classe = models.FloatField(null=True, blank=True)
    note_devoir = models.FloatField(null=True, blank=True)
    note_composition = models.FloatField(null=True, blank=True)
    moyenne_sur_20 = models.FloatField(null=True, blank=True)
    note_definitive = models.FloatField(null=True, blank=True)
    rang = models.CharField(max_length=10, blank=True)
    appreciation = models.ForeignKey(Appreciation, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} - {self.annee_academique} - {self.tranche_academique}"
