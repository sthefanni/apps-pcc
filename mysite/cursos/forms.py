from django.forms import ModelForm
from cursos.models import Cursos


class CursosForm(ModelForm):
    
    class Meta:
        model = Cursos
        fields = "__all__"