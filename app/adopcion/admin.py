# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.adopcion.models import Persona, Solicitud

# Register your models here.
admin.site.register(Persona)
admin.site.register(Solicitud)