from django.db import models
from cpf_field.models import CPFField

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    cpf = CPFField('cpf')

    def __str__(self):
        return self.nome
    
