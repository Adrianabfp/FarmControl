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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input-form'})

class EntregaForm(forms.Form):
    paciente = forms.CharField(label="Para quem", max_length=100)
    data_entrega = forms.DateField(label="Data da Entrega", widget=forms.DateInput(attrs={'type': 'date'}))
    quantidade = forms.IntegerField(label="Quantidade", min_value=1)
