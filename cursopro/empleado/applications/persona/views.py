from django.shortcuts import render

from django.views.generic import (
    ListView
)
#Models
from .models import Empleado

class ListAllEmpleados(ListView):
     template_name = 'persona/list_all.html'
     model = Empleado

class ListByAreaEmpleado(ListView):
    """ lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    
    def get_queryset(self):
        #el codigo que yo quiera
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
         departamento__name=area
     )
        return lista

class ListByJobEmpleado(ListView):
    """ lista empleados de un Trabajo """
    template_name = 'persona/list_by_job.html'
    context_object_name = 'Empleados'

    def get_queryset(self):
        #el codigo que yo quiera
        trabajo = self.kwargs['job']
        lista = Empleado.objects.filter(
        job__name = trabajo
    )
        return lista


# Create your views here.
# 1.- Listar todos los empleados de la empresa
# 2.- Listar todos los empleados que pertenecen a una area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
