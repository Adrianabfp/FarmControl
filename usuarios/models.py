from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    choices_cargo = (('G', 'Gestor'),
                     ('A', 'Atendente'))
    cargo = models.CharField(max_length=1, choices=choices_cargo, default='A')  # Default 'A' para Atendente
    # Campo para indicar se o Gestor está assumindo a função de Atendente temporariamente
    is_temporarily_atendente = models.BooleanField(default=False)

    email = models.EmailField('email address', unique=True, blank=False, null=False)

# Create your models here.
