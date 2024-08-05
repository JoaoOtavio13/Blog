from django.shortcuts import render
from .models import Curso,Modalidade
# Create your views here.
# fiz em sala 
def index(request):
    lista_cursos= Curso.objects.all()
    lista_modalidade=Modalidade.objects.all()
    context ={
        'cursos': lista_cursos
        'modalidades': lista_modalidade
    }
    return render(request, 'cursos/index.html')

def ads(request):
    return render(request, 'cursos/ads.html')

def alimentos(request):
    return render(request, 'cursos/alimentos.html')

def quimica(request):
    return render(request, 'cursos/quimica.html')

