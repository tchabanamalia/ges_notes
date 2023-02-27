from django.shortcuts import render
from django.http import HttpResponse
from notes.models import Eleve, Matiere, Niveau, Note
from django import forms
from notes.forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.http import FileResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from Templating_ifnti.controleur import generate_pdf, generate3_pdf


from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
	liste_eleves=Eleve.objects.all()
	list_matieres = Matiere.objects.all()
	list_niveaux = Niveau.objects.all()
	return render(request, "notes/index.html", locals())

def eleves(request):
	liste_eleves=Eleve.objects.all()
	context={"lesEleves":liste_eleves}
	return render(request, "notes/eleves.html", context)

def detailsEleves(request):
	liste_eleves=Eleve.objects.all()
	context={"lesEleves":liste_eleves}
	return render(request, "notes/detailsEleves.html", context)


def eleve(request, id):
	eleve = get_object_or_404(Eleve, id=id)
	return render(request, "notes/eleve.html", {"eleve":eleve})
	#return HttpResponse("Affichage des identifiants d'un seul élève")



def matieres(request):
	list_matieres = Matiere.objects.all()
	context={"lesMatieres":list_matieres}
	return render(request, "notes/matieres.html", context)
	
	#les_matieres="----La liste des matières-----" + "<br> "
	#for matiere in list_matieres:
	#	les_matieres = les_matieres + matiere.nom + "<br> "
	#return HttpResponse(les_matieres)

def matiere(request, id):
	matiere = get_object_or_404(Matiere, id=id)
	return render(request, "notes/matiere.html", {"matiere":matiere})

#def niveaux(request):
#	list_niveaux = Niveau.objects.all()
#	les_niveaux="----La liste des niveau-----" + "<br> "
#	for niveau in list_niveaux:
#		les_niveaux = les_niveaux + niveau.nom + "<br> "
#	return HttpResponse(les_niveaux)

def niveau(request, id):
	niveau = get_object_or_404(Niveau, id=id)
	return render(request, "notes/niveau.html", {"niveau":niveau})

@login_required
@permission_required('notes.add_note')
def add_note(request, eleve, matiere ):
	eleve = get_object_or_404(Eleve, id=eleve)
	matiere = get_object_or_404(Matiere, id=matiere)
	if request.method == "GET":
		return render(request, "notes/add_note.html")
	elif request.method == "POST":
		eleve.matieres.all()
		note1=Note(valeur=request.POST['valeur'], eleve=eleve, matiere=matiere)		
		note1.save()
		return HttpResponse("La note est enregistré avec succès.")
	else:
		return HttpResponse("La note n'a pas été enregistré.")



@login_required
@permission_required('notes.add_note')
def ajout_note(request, eleve, matiere):
	eleve = get_object_or_404(Eleve, id=eleve)
	matiere = get_object_or_404(Matiere, id=matiere)
    
	if request.method == "POST":
		form = NoteForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			valeur = form.cleaned_data['valeur']
			note1=Note(valeur=valeur, eleve=eleve, matiere=matiere)		
			note1.save()
			return HttpResponse("La note est enregistré avec succès.")
	form = NoteForm()
	context = {"form":form}
	return render(request,'notes/ajout_note.html', context)



def notes(request):
	liste_notes = Note.objects.all()
	context={"lesNotes":liste_notes}
	return render(request, "notes/notes.html", context)



def listeEleves(request):
	with open('out/rapport_Vues.pdf', 'rb') as pdf:
		reponse = HttpResponse(pdf.read(), content_type='application/pdf')
		reponse['Content-Disposition'] = 'inline;filename=rapport_Vues.pdf'
		return reponse



def listEleves(request):     
	liste_eleves=Eleve.objects.all()
	liste = []
	for elv in liste_eleves :
		dict_elv = {}
		dict_elv["matricule"]=elv.id
		dict_elv["nom"]=elv.nom
		dict_elv["prenom"]=elv.prenom
		dict_elv["sexe"]=elv.sexe
		dict_elv["dateNais"]=elv.date_naissance
		liste.append(dict_elv)
	context = {"eleves":liste}
	generate_pdf(context)

	with open('out/liste_eleves.pdf', 'rb') as pdf:
		reponse = HttpResponse(pdf.read(), content_type='application/pdf')
		reponse['Content-Disposition'] = 'inline;filename=liste_eleves.pdf'
		return reponse




def liste_niveauElv(request, id):
	niveau = get_object_or_404(Niveau, id=id)
	liste_eleves_par_niveau = niveau.eleve_set.all()
	#print(liste_eleves_par_niveau)

	liste = []
	for elv in liste_eleves_par_niveau :
		dict_elv = {}
		dict_elv["matricule"]=elv.id
		dict_elv["nom"]=elv.nom
		dict_elv["prenom"]=elv.prenom
		dict_elv["sexe"]=elv.sexe
		dict_elv["dateNais"]=elv.date_naissance
		dict_elv["niveau"]=elv.niveau
		liste.append(dict_elv)
	context = {"eleves":liste}
	generate_pdf(context)

	with open('out/liste_eleves_par_niveau.pdf', 'rb') as pdf:
		reponse = HttpResponse(pdf.read(), content_type='application/pdf')
		reponse['Content-Disposition'] = 'inline;filename=liste_eleves_par_niveau.pdf'
		return reponse



"""def noteEleves(request, id):
	matiere = get_object_or_404(Matiere, id=id)
	eleves = matiere.eleve_set.all()

	liste = []
	for eleve in eleves :
		dict_notes = {}
		note = 0
		_note = Note.objects.filter(eleve = eleve, matiere=matiere)
		if _note :
			note = _note[0]
		dict_notes["nom"]=eleve.nom
		dict_notes["prenom"]=eleve.prenom
		dict_notes["note"]=eleve.note
		liste.append(dict_notes)
	context={"lesNotes":liste}
	generate3_pdf(context)

	with open('out/noteEleves_par_matiere.pdf', 'rb') as pdf:
		reponse = HttpResponse(pdf.read(), content_type='application/pdf')
		reponse['Content-Disposition'] = 'inline;filename=noteEleves_par_matiere.pdf'
		return reponse
"""



def noteEleves(request, id_matiere):
	matiere = Matiere.objects.get(id=id_matiere)
	eleves = matiere.eleve_set.all()
	tab_eleve = []
	for eleve in eleves :
		note = 0
		_note = Note.objects.filter(eleve=eleve, matiere=matiere)
		if _note :
			note = _note[0]
		if note.valeur < 12 :
			validation = "Echec"
		else:
			validation = "valider"

		ele = {"nom" : eleve.nom, "prenom" : eleve.prenom, "note" : note.valeur, "validation" : validation}
		tab_eleve.append(ele)
		print(tab_eleve)
		context = {"eleves" : tab_eleve, "matiere" : matiere.nom}
		generate3_pdf(context)

		with open('out/noteEleves_par_matiere.pdf', 'rb') as pdf:
			reponse = HttpResponse(pdf.read(), content_type='application/pdf')
			reponse['Content-Disposition'] = 'inline;filename=noteEleves_par_matiere.pdf'
			return reponse



