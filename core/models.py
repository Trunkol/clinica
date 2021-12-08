from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    PACIENTE = 'paciente'
    MEDICO = 'medico'

    TIPOS_DISPONIVEIS = (
        (PACIENTE, PACIENTE),
        (MEDICO, MEDICO)
    )

    usuario = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    tipo = models.CharField('tipo', choices=TIPOS_DISPONIVEIS, max_length=255, default=PACIENTE)
    telefone = models.CharField('Telefone', max_length=255, null=True, blank=True)
    nome = models.CharField('nome', max_length=255, null=True, blank=True)

    def is_medico(self):
        return self.tipo == self.MEDICO
    
    def is_paciente(self):
        return self.tipo == self.PACIENTE

    def __str__(self):
        return self.nome

class Clinica(models.Model):
    endereco = models.CharField('Endereço', max_length=255)

class Medico(models.Model):
    profile = models.OneToOneField(Profile, related_name='profile', on_delete=models.CASCADE)
    clinica = models.OneToOneField(Clinica, related_name='clinica', on_delete=models.CASCADE)
    especialidade = models.CharField('Especialidade', blank=True, max_length=255, null=True)
    duracao_consulta = models.IntegerField('Duração da Consulta', default=60)

class Consulta(models.Model):
    medico = models.ForeignKey(Profile, related_name='medico', on_delete=models.CASCADE)
    paciente = models.ForeignKey(Profile, related_name='paciente', on_delete=models.CASCADE)
    horario_inicio = models.DateTimeField('Horário de Inicio', auto_now_add=True)
    horario_fim = models.DateTimeField('Horário Encerramento', blank=True, null=True)
