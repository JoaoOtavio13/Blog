from django.contrib import admin
from django.urls import path
from cursos.views import index, ads, alimentos, quimica 

urlpatterns=[
    path('', index, name='index'),
    path('ads/', ads, name='ads'),
    path('alimentos/', alimentos,name='alimentos'),
    path('quimica/', quimica, name='quimica'),
]