# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from app.mascota.form import MascotaForm
from app.mascota.models import Mascota
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

# Create your views here.
def index(req):
    return render(req, 'mascotas/index.html')

def mascota_view(req):
    if req.method == 'POST':
        form = MascotaForm(req.POST)
        if (form.is_valid()):
            form.save()
        return redirect('mascota:mascota_listar')
    else:
        form = MascotaForm()
    return render(req, 'mascotas/mascotas_form.html', {'form':form})

def mascota_list(req):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(req, 'mascotas/mascotas_list.html', contexto)

def mascota_edit(req, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if req.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(req.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(req, 'mascotas/mascotas_form.html', {'form':form})

def mascota_delete(req, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if req.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(req, 'mascotas/mascota_delete.html', {'mascota':mascota})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascotas/mascotas_list.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascotas_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascotas/mascotas_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaDelte(DeleteView):
    model = Mascota
    template_name = 'mascotas/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')