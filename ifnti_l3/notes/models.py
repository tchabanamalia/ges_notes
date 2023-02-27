from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


# Create your models here.

class Personne(models.Model):  
    SEXE_CHOISE = [
        ('F','Feminin'),
        ('M','Masculin')
    ]
    nom=models.CharField(max_length=50) 
    prenom = models.CharField(max_length=50, verbose_name="Prénom") 
    sexe = models.CharField(max_length=1, choices=SEXE_CHOISE)
    date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.nom) + ' ' + str(self.prenom) 


class Enseignant(Personne):
    pass

class Matiere(models.Model):
    nom=models.CharField(max_length=50, unique=True) 
    enseignant = models.ForeignKey('Enseignant', on_delete=models.CASCADE)
    niveau = models.ManyToManyField("Niveau")

    def __str__(self):
        return str(self.nom) 
    class Meta:
        verbose_name_plural = "Matières"

class Eleve(Personne):
    id = models.IntegerField(primary_key=True)
    niveau = models.ForeignKey('Niveau', on_delete=models.CASCADE)
    matieres = models.ManyToManyField("Matiere", verbose_name="Matières", blank=True)

    def save(self, *args, **kwargs):
        #if self.matieres == "" or self.matieres == "null":
         #   el_mat = self.niveau.matieres
          #  self.matieres = el_mat
        if not self.matieres.all():
            for matiere in self.niveau.matiere_set.all():
               # print(matiere)
                self.matieres.add(matiere)        
        super().save(*args, **kwargs)


    
    def __str__(self):
        return  str(self.nom) + ' ' + str(self.prenom) 
    class Meta:
        verbose_name_plural = "Élèves"


class Niveau(models.Model):
    nom = models.CharField(max_length=50, unique=True)                

    def __str__(self):
        return str(self.nom)

    class Meta:
        verbose_name_plural = "Niveaux"


class Note(models.Model):
    valeur=models.FloatField(null=True, validators=[MinValueValidator(0.0), MaxValueValidator(20.0)])
    eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE)
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE)
   
    def __str__(self):
        return str(self.valeur) + ' ' + str(self.eleve) + ' ' + str(self.matiere)






    
