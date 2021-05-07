from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from cadastro.models import Cliente
from cadastro.serializer import ClienteSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer