from django import forms
from django_select2.forms import ModelSelect2Widget, ModelSelect2MultipleWidget, Select2Widget
from django.contrib.auth.models import User
from core.models import Profile, Medico

class CriarUsuário(forms.ModelForm):
    email = forms.EmailField(label='E-mail', required=True, widget=forms.TextInput(
                attrs={'placeholder': 'email@server.com', 'class': "form-control"}))
    nome = forms.CharField(label='Nome', required=True, widget=forms.TextInput(attrs={'placeholder': 'nome', 'class': "form-control"}))
    telefone = forms.CharField(label='Telefone', required=True, widget=forms.TextInput(attrs={'placeholder': '(00) 00000-00000 ', 'class': "form-control", 'data-toggle': 'input-mask', 'data-mask-format': '(00) 00000-0000'}), help_text='Esse número será utilizado para as notificações da plataforma')
    tipo_perfil = forms.ChoiceField(label='Tipo de Usuário', choices=Profile.TIPOS_DISPONIVEIS, required=True, widget=Select2Widget(attrs={'data-placeholder': 'Escolha o seu tipo de usuário', 'class': 'form-control'}))
    new_password1 = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(attrs={'placeholder': '************ ', 'class': "form-control"}))
    new_password2 = forms.CharField(label='Confirmação da senha', required=True, widget=forms.PasswordInput(attrs={'placeholder': '************ ', 'class': "form-control"}))

    class Meta:
        model = Profile
        fields = ('nome', 'email', 'telefone', 'tipo_perfil', 'new_password1', 'new_password2')

    #def clean(self):
    #    password1 = self.cleaned_data.get('new_password1')
    #    password2 = self.cleaned_data.get('new_password2')
    #    if password1 and password2 and password1 != password2:
    #        self.add_error('new_password1', u'As senhas não são iguais!')
    #        self.add_error('new_password2', u'As senhas não são iguais!')
    #
    #    email = self.cleaned_data.get('email')
    #    if User.objects.filter(username=email).exists():
    #        self.add_error('email', u'Já existe um usuário cadastrado com esse e-mail')
    #
    #    return self.cleaned_data

    def save(self):
        password = self.cleaned_data.get('new_password1')
        email = self.cleaned_data.get('email')
        user = User.objects.create_user(username=email,
                                 email=email,
                                 password=password)

        profile = Profile.objects.create(
            usuario=user, telefone=self.cleaned_data.get('telefone')
        )
        if self.cleaned_data.get('tipo_perfil') == Profile.MEDICO:
            profile.tipo_perfil = Profile.MEDICO,
            profile.save()
        return user