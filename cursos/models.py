from django.db import models

# Create your models here.
#fiz em sala 
def Modalidade(models.Model):
    nome= models.Charfield(max_length=150)

    def __str__(self):
        return self.nome

def Curso(models.Model):
    nome= models.Charfield(max_length=150)

    def __str__(self):
        return self.nome