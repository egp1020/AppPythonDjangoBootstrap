from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView


from .models import Libro

def home(request):
    return render(request, 'index.html')


class ListarLibros(ListView):
    model=Libro
    template_name='libros/listar_libros.html'


class CrearLibro(CreateView):
    model=Libro
    template_name='libros/crear_libro.html'
    success_url='/libros'
    fields=['nombre', 'autor', 'fecha_publicacion']


class EditarLibro(UpdateView):
    model=Libro
    template_name='libros/editar_libro.html'
    success_url='/libros'
    fields=['nombre', 'autor', 'fecha_publicacion']


class EliminarLibro(DeleteView):
    model=Libro
    template_name='libros/eliminar_libro.html'
    success_url='/libros'


class MostrarLibro(DetailView):
    model=Libro
    template_name='libros/mostrar_libro.html'

