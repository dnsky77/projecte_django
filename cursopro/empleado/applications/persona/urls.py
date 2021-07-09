from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('lista-by-area/<shorname>', views.ListByAreaEmpleado.as_view()),
    path('lista-by-job/<name>', views.ListByJobEmpleado.as_view()),
    path('buscar-empleado', views.ListEmpleadosByKword.as_view()),
]