from django import forms
from notes.models import Matiere, Note, Eleve
from django.core.exceptions import ValidationError




class NoteForm(forms.ModelForm):
   class Meta:
     model = Note
     fields = ["valeur"]
     labels = {"valeur": "Note sur 20"}


class EleveForm(forms.ModelForm):
  class Meta:
    model = Eleve
    fields = '__all__'
    nom = forms.CharField()



  def clean(self):
    cleaned_data = super().clean()
  #  matieres = self.cleaned_data['matieres']
    niveau = self.cleaned_data['niveau']
    nom = self.cleaned_data['nom']
    if not nom.isalpha():
      raise forms.ValidationError('Le nom ne peut contenir que des lettres.')
   # for matiere in matieres : 
    #  if matiere not in niveau.matiere_set.all():
      #  raise ValidationError("la matière n'est pas enseigné dans ce niveau")
      
