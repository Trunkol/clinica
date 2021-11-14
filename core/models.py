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

    user = models.OneToOneField(User, related_name='profile')
    type = models.CharField('type', choices=TIPOS_DISPONIVEIS, max_length=255, default=PACIENTE)