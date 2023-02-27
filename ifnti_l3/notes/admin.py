from django.contrib import admin
from .models import Enseignant, Matiere, Eleve, Niveau, Note
from notes.forms import EleveForm


admin.site.register(Enseignant)
admin.site.register(Matiere)
#admin.site.register(Eleve)
admin.site.register(Niveau)
admin.site.register(Note)




class EleveAdmin(admin.ModelAdmin):
    model = Eleve
    empty_value_display = '---'
    list_per_page = 2
    raw_id_fields = ['matieres']
    form = EleveForm
admin.site.register(Eleve, EleveAdmin)

