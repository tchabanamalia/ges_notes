from django.urls import path
from . import views
app_name="notes"
urlpatterns = [
	path('', views.index, name='index'),
	path('eleves/', views.eleves, name='eleves'),
	path('detailsEleves/', views.detailsEleves, name='detailsEleves'),
	path('eleve/<int:id>', views.eleve, name='eleve'),
	path('matieres/', views.matieres, name='matieres'),
	path('matiere/<int:id>', views.matiere, name='matiere'),
	path('niveau/<int:id>', views.niveau, name='niveau'),
	path('add_note/<int:eleve>/<int:matiere>', views.add_note, name='add_note'),
	path('notes/', views.notes, name='notes'),
	path('ajout_note/<int:eleve>/<int:matiere>', views.ajout_note, name='ajout_note'),
	path('listeEleves/', views.listeEleves, name='listeEleves'),
	path('liste_niveauElv/<int:id>', views.liste_niveauElv, name='liste_niveauElv'),
	path('noteEleves/<int:id_matiere>', views.noteEleves, name='noteEleves'),

]

