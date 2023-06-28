from django.urls import path, include
from AppCoder.views import  *

urlpatterns = [
    path('inicio/', inicio),
    path('cursos/', cursos, name="Cursos"),
    path('entregables/', entregables, name="Entregables"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('setEstudiantes/', setEstudiantes, name="SetEstudiantes"),
    path('getEstudiante/', getEstudiante, name="GetEstudiante"),
    path('buscarEstudiante/', buscarEstudiante, name="BuscarEstudiante")
]   