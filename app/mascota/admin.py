# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.mascota.models import Mascota, Vacuna

# Register your models here.
admin.site.register(Vacuna)
admin.site.register(Mascota)