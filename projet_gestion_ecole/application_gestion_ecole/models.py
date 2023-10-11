from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, nom, prenom, sexe, username, email, password):
        # Crée un utilisateur avec les champs fournis
        user = self.model(
            nom=nom,
            prenom=prenom,
            sexe=sexe,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nom, prenom, sexe, username, email, password):
        # Crée un superutilisateur avec les champs fournis
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

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nom', 'prenom', 'email', 'sexe']

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    

class Classe(models.Model):
    code = models.CharField(max_length=10, unique=True)
    libelle = models.CharField(max_length=25, unique=True)

class Matiere(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=50)

class Eleve(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    cle = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    sexe = models.SmallIntegerField()

class Professeur(models.Model):
    code = models.CharField(max_length=10, unique=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    classes = models.ManyToManyField('Classe', through='ProfesseurClasse')

class ProfesseurClasse(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee_academique = models.IntegerField(default=0)
    tranche_academique = models.IntegerField(default=0)
    titulaire = models.BooleanField(default=False)

class Appartenance(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)

class Appreciation(models.Model):
    intervalle1 = models.CharField(max_length=5, default='0')
    libelle = models.CharField(max_length=25)
    intervalle2 = models.CharField(max_length=5, default='0')
    couleur = models.CharField(max_length=10)

class Composition(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    annee_academique = models.IntegerField()
    tranche_academique = models.IntegerField()
    appreciation = models.ForeignKey(Appreciation, on_delete=models.CASCADE)
    note_classe = models.FloatField(null=True)
    note_devoir = models.FloatField(null=True)
    note_composition = models.FloatField(null=True)
    moyenne_sur_20 = models.FloatField(null=True)
    note_definitive = models.FloatField(null=True)
    rang = models.CharField(max_length=10)
    appreciation_textuelle = models.CharField(max_length=50)
