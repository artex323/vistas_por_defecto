from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from .models import Libro


class CrearLibro(SuccessMessageMixin,CreateView):
    model= Libro
    form= Libro
    fields = "__all__"
    success_message = 'Libro Creado Correctamente !'

class ListarLibro(ListView):
    model = Libro

class DetalleLibro(DetailView):
    model = Libro

class ActualizarLibro(SuccessMessageMixin,UpdateView):
    model= Libro
    form= Libro
    fields = "__all__"
    success_message = 'Libro Actualizado Correctamente !'

    def get_success_url(self):
        return reverse('leer')

class EliminarLibro(SuccessMessageMixin,CreateView):
    model= Libro
    form= Libro
    fields = "__all__"

    def get_success_url(self):
        success_message ='Libro Eliminado Correctamente !'
        messages.success (self.request, (success_message))
        return reverse('leer')