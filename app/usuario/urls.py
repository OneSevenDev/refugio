from django.conf.urls import url
from app.usuario.views import RegistroUsuario, UserAPI

urlpatterns = [
    url(r'^register$', RegistroUsuario.as_view(), name="registrar"),
    url(r'^api', UserAPI.as_view(), name="api"),
]