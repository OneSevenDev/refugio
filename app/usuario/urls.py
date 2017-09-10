from django.conf.urls import url
from app.usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^register$', RegistroUsuario.as_view(), name="registrar"),
]