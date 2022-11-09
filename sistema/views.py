from rest_framework import viewsets
from sistema.models import Produtor, Produto, Pedido, Relatorio
from sistema.serializer import ProdutoSerializer, ProdutorSerializer, PedidoSerialiser, RelatorioSerialiser
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProdutoresViewSet(viewsets.ModelViewSet):
    """Exibindo Produtores do Sistema"""
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo Produtos do Sistema"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    """Exibindo Pedidos do Sistema"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerialiser


class RelatorioViewSet(viewsets.ModelViewSet):
    """Exibindo Pedidos do Sistema"""
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerialiser

