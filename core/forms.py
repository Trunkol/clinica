from typing import final
from django import forms
from django_select2.forms import ModelSelect2Widget
from core.models import Profile, Consulta
from datetime import datetime

class ConsultaForm(forms.Form):
    medico = forms.ModelChoiceField(label='Médico', queryset=Profile.objects.filter(tipo=Profile.MEDICO), required=True,
                                       widget=ModelSelect2Widget(model=Profile, search_fields=['nome__icontains'],
                                                                 attrs={'class': "form-control", "data-minimum-input-length": "0", "data-placeholder": "Busque e selecione um médico"}))
    inicio_da_consulta = forms.CharField(initial=datetime.now().strftime("%H:%M:%S %d/%m/%Y"), required=True, widget=forms.TextInput(
                                        attrs={'placeholder': '', 'class': "form-control"}))
    final_da_consulta = forms.CharField(initial=datetime.now().strftime("%H:%M:%S %d/%m/%Y"), required=True, widget=forms.TextInput(
                                        attrs={'placeholder': '', 'class': "form-control"}))

    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile', None)
        super(ConsultaForm, self).__init__(*args,**kwargs)
    
    def clean(self):
        pass

    def save(self):
        inicio_da_consulta = datetime.strptime(self.cleaned_data.get('inicio_da_consulta'), "%H:%M:%S %d/%m/%Y")
        final_da_consulta = datetime.strptime(self.cleaned_data.get('final_da_consulta'), "%H:%M:%S %d/%m/%Y")
        
        return Consulta.objects.create(
            medico=self.cleaned_data.get('medico'),
            paciente=self.profile,
            horario_inicio=inicio_da_consulta,
            horario_fim=final_da_consulta
        )