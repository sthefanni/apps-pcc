from django.forms import ModelForm
from conteudo.models import Conteudo


class ConteudoForm(ModelForm):
    
    class Meta:
        model = Conteudo
        fields = "__all__"