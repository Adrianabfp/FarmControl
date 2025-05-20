from django import forms
from .models import Produto, Medicamento

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome', 'dosagem', 'categoria', 'quantidade','data_validade', 'ultima_compra' ]

