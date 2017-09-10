import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from rest_framework.views import APIView

from app.usuario.forms import RegistroForm
from app.usuario.serializers import UserSerializer


# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('mascota:mascota_listar')

class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, req, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')