from django import forms
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget, Select2Widget
from django.contrib.auth.models import User

class CriarUsuário(forms.ModelForm):
    email = forms.EmailField(label='E-mail', required=True, widget=forms.TextInput(
                attrs={'placeholder': 'email@server.com', 'class': "form-control"}))
    nome = forms.CharField(label='Nome do Profissional', required=True, widget=forms.TextInput(attrs={'placeholder': 'nome', 'class': "form-control"}))
    telefones = forms.CharField(label='Telefone', required=True, widget=forms.TextInput(attrs={'placeholder': '(00) 00000-00000 ', 'class': "form-control", 'data-toggle': 'input-mask', 'data-mask-format': '(00) 00000-0000'}), help_text='Esse número será utilizado para as notificações da plataforma')
    new_password1 = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(attrs={'placeholder': '************ ', 'class': "form-control"}))
    new_password2 = forms.CharField(label='Confirmação da senha', required=True, widget=forms.PasswordInput(attrs={'placeholder': '************ ', 'class': "form-control"}))

    class Meta:
        model = PessoaFisica
        fields = ('nome', 'email', 'telefones', 'new_password1', 'new_password2')

    def clean(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2 and password1 != password2:
            self.add_error('new_password1', u'As senhas não são iguais!')
            self.add_error('new_password2', u'As senhas não são iguais!')

        email = self.cleaned_data.get('email')
        if User.objects.filter(username=email).exists():
            self.add_error('email', u'Já existe um usuário cadastrado com esse e-mail')

        return self.cleaned_data
