from rest_framework import viewsets, generics
from sistema.models import Produtor, Produto, Pedido, Relatorio
from sistema.serializer import ProdutoSerializer, ProdutorSerializer, PedidoSerialiser, RelatorioSerialiser, ListaPedidosProdutorSerializer
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

class ListaPedidosProdutorViewSet(generics.ListAPIView):
    "Listando os Pedidos Feitos a um Prdutor"
    def get_queryset(self):
        queryset = Pedido.objects.filter(produtor_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPedidosProdutorSerializer
