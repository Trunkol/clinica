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

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    type = models.CharField('type', choices=TIPOS_DISPONIVEIS, max_length=255, default=PACIENTE)

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)